from sqlalchemy import Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[str]= mapped_column(String, nullable=True)

    reviews= relationship('Review', back_populates='movie')

    def __str__(self):
        return f'Movie: {self.title}'


