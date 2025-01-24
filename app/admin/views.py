from sqladmin import ModelView
from app.users.models import User


class UserAdmin(ModelView, model= User):
    column_list=[User.id, User.email,User.name]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False
    name= "User"
    name_plural= "Users"
    icon= 'fa-solid fa-user'
    page_size = 10
    page_size_options = [10,25,50]