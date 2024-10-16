from datetime import date
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    birthday: date


class UserCreate(schemas.BaseUserCreate):
    birthday: date


class UserUpdate(schemas.BaseUserUpdate):
    birthday: date