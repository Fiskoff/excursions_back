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

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning("Verification requested for user %r. Verification token: %r", user.id, token)
