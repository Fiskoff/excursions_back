from fastapi import FastAPI
from fastapi import APIRouter

from app.router.auth_router import auth_router


app = FastAPI()

router = APIRouter(
    prefix="/excursions",
    tags=["Excursions"]
)
router.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)