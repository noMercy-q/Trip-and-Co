import uuid

from app import schemas
from db.client import PostgresClient
from db.user_repo import UserRepository

from passlib.context import CryptContext


class AuthService:
    user_repo: UserRepository

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register_user(self, user: schemas.Register) -> uuid.UUID:
        return await self.user_repo.create(schemas.UserCreate(
            name=user.name,
            email=user.email,
            password_hash=self.pwd_context.hash(user.password)
        ))

    async def login_user(self, user: schemas.Login) -> schemas.User | None:
        usr = await self.user_repo.get_by_credentials(user.email)

        if not usr:
            return None

        if not self.pwd_context.verify(user.password, usr.password_hash):
            return None

        return usr
