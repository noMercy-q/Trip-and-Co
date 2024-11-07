import os
import uuid
from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from app.routes.utils import JWT_SECRET_KEY, JWT_ALGORITH


# class JWTMiddleware(BaseHTTPMiddleware):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     async def dispatch(self, request: Request, call_next):
#         auth_header: str | None = request.headers.get("Authorization")
#
#         if auth_header:
#             token = auth_header.split(" ")[1]  # Извлечение токена после "Bearer "
#             try:
#                 payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITH])
#                 # Сохраняем user_id в request.state, чтобы использовать в обработчиках
#                 request.state.user_id = uuid.UUID(payload.get("user_id"))
#             except jwt.DecodeError:
#                 raise HTTPException(
#                     status_code=HTTP_403_FORBIDDEN, detail="Invalid or expired token"
#                 )
#         else:
#             request.state.user_id = None  # Если токен отсутствует
#
#         return await call_next(request)
