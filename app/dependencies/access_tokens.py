from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from core.config.database_helper import db_helper
from app.models.access_token import AccessToken


async def get_access_token_db(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    yield AccessToken.get_db(session=session)