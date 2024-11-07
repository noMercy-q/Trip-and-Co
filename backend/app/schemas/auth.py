from datetime import datetime

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str

class Login(BaseModel):
    email: EmailStr
    password: str

class Register(BaseModel):
    email: EmailStr
    name: str
    password: str

class TokenPayloadData(BaseModel):
    user_id: str
    name: str
    email: str
    exp: datetime | None
