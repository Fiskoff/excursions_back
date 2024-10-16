from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from app.models.access_token import AccessToken
from app.dependencies.access_tokens import get_access_token_db
from core.config.config_project import settings



def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_seconds
    )