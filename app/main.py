from fastapi import FastAPI, Depends
from fastapi import APIRouter
from fastapi.security import HTTPBearer

from app.router.auth_router import auth_router
from app.router.register_router import register_router
from app.router.user_router import user_router


app = FastAPI()

http_bearer = HTTPBearer(auto_error=False)
main_router = APIRouter(
    prefix="/excursion",
    dependencies=[Depends(http_bearer)],
)
main_router.include_router(auth_router)
main_router.include_router(register_router)
main_router.include_router(user_router)


app.include_router(main_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
