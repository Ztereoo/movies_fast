from app.reviews.models import Review
from dao.base import BaseDao


class ReviewDao(BaseDao):
    model = Review
