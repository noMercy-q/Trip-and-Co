import os
import secrets
import string
from datetime import timedelta, datetime
from typing import Optional

import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from app import schemas

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITH = "HS256"


security = HTTPBearer()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    print(to_encode, JWT_SECRET_KEY, JWT_ALGORITH)
    encoded_jwt = jwt.encode(to_encode, key=JWT_SECRET_KEY, algorithm=JWT_ALGORITH)
    return encoded_jwt


def get_current_user(auth: HTTPAuthorizationCredentials = Depends(security)) -> schemas.TokenPayloadData:
    token = auth.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITH])

        return schemas.TokenPayloadData(**payload)
    except jwt.DecodeError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Invalid or expired token"
        )

def generate_invite_token(length):
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for _ in range(length))
    return token