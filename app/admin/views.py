from sqladmin import ModelView

from app.movies.models import Movie
from app.reviews.models import Review
from app.users.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.name]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False
    name = "User"
    name_plural = "Users"
    icon = 'fa-solid fa-user'
    page_size = 10
    page_size_options = [10, 25, 50]


class MovieAdmin(ModelView, model=Movie):
    column_list = [c.name for c in Movie.__table__.c]
    name = "Movie"
    name_plural = "Movies"
    page_size = 10
    page_size_options = [10, 25, 50]


class ReviewAdmin(ModelView, model=Review):
    column_list = [c.name for c in Review.__table__.c]+ [Review.user]+ [Review.movie]
    name='Review'
    name_plural = 'Reviews'
    page_size = 10
    page_size_options = [10, 25, 50]

