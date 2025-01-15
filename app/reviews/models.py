from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, ForeignKey, Text, Float


class Review(Base):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey('movies.id'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    сomment: Mapped[str] = mapped_column(Text)

    # movie: Mapped['Movie'] = relationship('Movie', back_populates='reviews')
    # user: Mapped['User'] = relationship('User', back_populates='reviews')
