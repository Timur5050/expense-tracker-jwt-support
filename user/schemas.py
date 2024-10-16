from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    password: str


class UserRetrieveSchema(BaseModel):
    id: int
    username: str
    date_joined: datetime
    last_login: datetime
