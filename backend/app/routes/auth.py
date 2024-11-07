from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette.status import HTTP_403_FORBIDDEN

from app import schemas, auth_service
from app.routes.utils import create_access_token, get_current_user

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login", tags=['auth'])
async def login(user: schemas.Login) -> schemas.Token:
    user = await auth_service.login_user(user)

    if not user:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "user_id": str(user.id),
            "name": user.name,
            "email": user.email,
        }
    )

    return schemas.Token(access_token=token)


@auth_router.post("/register", tags=['auth'])
async def register(user: schemas.Register) -> schemas.Token:
    user_id = await auth_service.register_user(user)

    token = create_access_token(
        {
            "user_id": str(user_id),
            "name": user.name,
            "email": user.email,
        },
    )

    return schemas.Token(access_token=token)


@auth_router.get("/me", tags=['auth'])
async def me(user: schemas.TokenPayloadData = Depends(get_current_user)):
    return user
