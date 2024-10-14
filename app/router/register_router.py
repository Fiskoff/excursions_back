from fastapi import APIRouter

from app.dependencies.authentication.fastapi_users import fastapi_users
from app.schemas.user_schemas import UserRead, UserCreate

register_router = APIRouter(
    prefix="/register",
    tags=["Registration"]
)

register_router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)