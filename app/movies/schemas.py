from pydantic import BaseModel, EmailStr
from typing import Optional


class SMovies(BaseModel):
    title: str
    description: str
    year: int
    genre: str


class SUpdate(SMovies):
    title: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
