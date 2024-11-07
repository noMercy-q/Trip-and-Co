import uuid

from sqlalchemy import insert, select

from app import schemas
from db.client import PostgresClient
from db.models import User


class UserRepository:
    __client: PostgresClient

    def __init__(self, client: PostgresClient):
        self.__client = client

    async def create(self, user: schemas.UserCreate) -> uuid.UUID:
        async with self.__client.async_session() as sess:
            async with sess.begin():
                stmt = (
                    insert(User)
                    .values(**user.model_dump())
                    .returning(User.id)
                )

                res = (await sess.execute(stmt)).scalar_one()
                await sess.commit()

                return res

    async def get_by_credentials(self, email: str) -> schemas.User | None:
        async with self.__client.async_session() as sess:
            async with sess.begin():
                stmt = (
                    select(User)
                    .where(User.email == email)
                )

                user = (await sess.execute(stmt)).scalar_one_or_none()

                if user is None:
                    return None

                return schemas.User(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password_hash=user.password_hash,
                    created_at=user.created_at
                )