from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from core.config.database_helper import db_helper
from app.models.user_model import User


async def get_user_db(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    yield User.get_db(session=session)

