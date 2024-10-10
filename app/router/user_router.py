from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user_services import UserService
from app.config.database import async_session_maker

router = APIRouter(
    prefix="/register",
    tags=["Register User"]
)


async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session

@router.post("/")
async def register(username: str, password: str, email: str = None, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    try:
        await user_service.register_user(username, password, email)
        return {"message": "Пользователь успешно зарегистрирован"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Ошибка при регистрации пользователя")