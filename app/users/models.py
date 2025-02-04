from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str]= mapped_column(String,unique=True, nullable=False)
    hashed_password: Mapped[str]= mapped_column(String, nullable=False)

    reviews= relationship('Review', back_populates='user')

    def __str__(self):
        return  f"User: {self.email}"