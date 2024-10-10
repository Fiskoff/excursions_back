from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base, int_pk


class UsersORM(Base):
    __tablename__ = "user"

    id: Mapped[int_pk]
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[bytes] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=True)
    active: Mapped[bool] = True
