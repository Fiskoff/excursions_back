from fastapi import APIRouter

from app.dependencies.authentication.fastapi_users import fastapi_users


reset_password_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

reset_password_router.include_router(
    fastapi_users.get_reset_password_router(),
)