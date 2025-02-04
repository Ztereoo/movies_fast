from app.users.models import User
from dao.base import BaseDao


class UserDao(BaseDao):
    model = User
