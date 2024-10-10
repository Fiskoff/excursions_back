from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.user_repository import UserRepository
from app.models.user_model import UsersORM
from app.auth.utils import hash_password


class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def register_user(self, username: str, password: str, email: str = None):
        existing_user = await self.user_repository.get_user_by_username_or_email(username, email)

        if existing_user:
            raise ValueError("Пользователь с таким именем или email уже существует")

        hashed_password = hash_password(password)

        new_user = UsersORM(username=username, password=hashed_password, email=email)
        await self.user_repository.add_user(new_user)