from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user_model import UsersORM


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_username_or_email(self, username: str, email: str):
        stmt = select(UsersORM).where(
            (UsersORM.username == username) | (UsersORM.email == email)
        )
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def add_user(self, user: UsersORM):
        self.db.add(user)
        await self.db.commit()
