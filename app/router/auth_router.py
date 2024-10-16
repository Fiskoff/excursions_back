from fastapi import APIRouter

from app.dependencies.authentication.backand import authentication_backend
from app.dependencies.authentication.fastapi_users import fastapi_users

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

auth_router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)


