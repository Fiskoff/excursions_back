from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class AccessTokenConfig(BaseModel):
    lifetime_seconds: int = 3600


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: int
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"


    access_token: AccessTokenConfig = AccessTokenConfig()


settings = Settings()