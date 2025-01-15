from sqlalchemy import Integer, String
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship



class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str]= mapped_column(String,unique=True, nullable=False)
    hashed_password: Mapped[str]= mapped_column(String, nullable=False)

    # reviews: Mapped[list['Review']] = relationship('Review', back_populates='user')
