from datetime import date

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Date

from core.config.database import Base


class User(Base, SQLAlchemyBaseUserTable[int]):
    birthday: Mapped[date] = mapped_column(Date, nullable=False)

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, User)