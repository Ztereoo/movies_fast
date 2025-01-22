from app.database import Base
from sqlalchemy import String,Integer,func,Float
from sqlalchemy.orm import relationship, Mapped, mapped_column



class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[str]= mapped_column(String, nullable=True)



    # @hybrid_property
    # def average_rating(self) -> float:
    #     if self.reviews:
    #      return sum(review.rating for review in self.reviews)/len(self.reviews)
    #     return 0.0
