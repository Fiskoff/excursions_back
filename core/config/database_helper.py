from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from core.config.config_project import settings


DATABASE_URL = (f"postgresql+asyncpg://"
                f"{settings.env.DB_USER}:{settings.env.DB_PASS}@{settings.env.DB_HOST}:{settings.env.DB_PORT}/{settings.env.DB_NAME}")


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class DatabaseHelper:
    def __init__(
            self,
            url: str = DATABASE_URL,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10
    ) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size
        )

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper()