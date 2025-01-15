from dao.base import BaseDao
from app.movies.models import Movie

class Movies_Dao(BaseDao):
    model=Movie
