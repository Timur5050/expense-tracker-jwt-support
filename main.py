from typing import Annotated

import jwt
from fastapi import FastAPI, Cookie, Request, Response, HTTPException
from fastapi.responses import JSONResponse

from user import router as user_router
from auth.utils import decode_jwt
from expense import router as expense_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(expense_router.router)


@app.get("/")
async def root(request: Request):
    headers = request.headers
    token = headers.get("Authorization").replace("Bearer ", "")
    try:
        content = decode_jwt(token)
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired token")

    response = JSONResponse(content=content)
    response.set_cookie(key="hello", value="how are you")
    return response
