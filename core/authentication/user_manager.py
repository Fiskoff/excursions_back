from logging import getLogger
from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from app.models.user_model import User
from core.config.config_project import settings


log = getLogger(__name__)

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.env.reset_password_token_secret
    verification_token_secret = settings.env.verification_token_secret

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning("User %r has registered.", user.id)
