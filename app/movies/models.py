from sqlalchemy import Integer, String, select, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property

from app.reviews.models import Review
from app.database import Base


class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[str]= mapped_column(String, nullable=True)

    reviews= relationship('Review', back_populates='movie')

    average_rating = column_property(
        select(func.coalesce(func.avg(Review.rating), 0))
        .where(Review.movie_id == id)
        .correlate_except(Review)
        .scalar_subquery()
    )
    def __str__(self):
        return f'Movie: {self.title}'


