from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase,SQLAlchemyBaseAccessTokenTable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

from core.config.database_helper import Base


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyAccessTokenDatabase(session, AccessToken)
