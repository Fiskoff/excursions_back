from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column

from app.config.config import settings

DATABASE_URL = (f"postgresql+asyncpg://"
                f"{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

int_pk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    pass
