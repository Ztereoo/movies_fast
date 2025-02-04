from typing import Optional

from pydantic import BaseModel, EmailStr


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
