from fastapi_users import FastAPIUsers

from app.models.user_model import User
from app.dependencies.authentication.user_manager import get_user_manager
from app.dependencies.authentication.backand import authentication_backend


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend]
)