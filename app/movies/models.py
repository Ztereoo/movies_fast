from sqlalchemy import Integer, String, func, select
from sqlalchemy.orm import Mapped, column_property, mapped_column, relationship

from app.database import Base
from app.reviews.models import Review


class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[str] = mapped_column(String, nullable=True)

    reviews = relationship("Review", back_populates="movie")

    average_rating = column_property(
        select(func.coalesce(func.avg(Review.rating), 0))
        .where(Review.movie_id == id)
        .correlate_except(Review)
        .scalar_subquery()
    )

    def __str__(self):
        return f"Movie: {self.title}"
