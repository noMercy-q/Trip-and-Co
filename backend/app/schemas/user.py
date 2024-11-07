import uuid
from datetime import datetime

from aiohttp import streamer
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password_hash: str


class User(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    password_hash: str
    created_at: datetime
