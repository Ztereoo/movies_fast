from app.movies.models import Movie
from dao.base import BaseDao


class Movies_Dao(BaseDao):
    model = Movie
