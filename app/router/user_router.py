from fastapi import APIRouter

from app.dependencies.authentication.fastapi_users import fastapi_users
from app.schemas.user_schemas import UserRead, UserUpdate

user_router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

user_router.include_router(
    router=fastapi_users.get_users_router(UserRead, UserUpdate),
)
