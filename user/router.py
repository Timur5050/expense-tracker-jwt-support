import jwt
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from user import crud
from user.models import User
from user.schemas import UserSchema, UserRetrieveSchema
from dependenies import get_db
from auth.utils import get_password_hash, encode_jwt, decode_jwt, verify_password

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register/", response_model=UserRetrieveSchema)
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    user_in_db = db.query(User).filter(User.username == user.username).first()
    if user_in_db:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    password = get_password_hash(user.password)
    user.password = password

    return crud.create_user(db, user)


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


@router.post("/login/")
def login_user(user: UserSchema, db: Session = Depends(get_db)):
    user_in_db = authenticate_user(user.username, user.password, db)
    if not user_in_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_payload = {
        "username": user.username,
        "user_id": user_in_db.id,
        "token_type": "access"
    }
    refresh_payload = {
        "username": user.username,
        "user_id": user_in_db.id,
        "token_type": "refresh"
    }
    access_token = encode_jwt(access_payload)
    refresh_token = encode_jwt(refresh_payload, expire_minutes=1440)
    response_content = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    response = JSONResponse(content=response_content)
    response.set_cookie(key="access_token", value=access_token)
    response.set_cookie(key="refresh_token", value=refresh_token)
    return response


@router.post("/token/refresh/")
async def refresh_old_token(request: Request):
    body = await request.json()
    refresh_token = body.get("refresh_token")
    try:
        payload = decode_jwt(token=refresh_token)
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token expired")

    new_payload = {
        "username": payload.get("username"),
        "user_id": payload.get("user_id"),
        "token_type": "access"
    }
    new_access_token = encode_jwt(payload=new_payload)
    content = {
        "access_token": new_access_token,
    }

    response = JSONResponse(content=content)
    response.set_cookie(key="access_token", value=new_access_token)
    return response
