from pydantic import BaseModel, EmailStr
from typing import Optional
class SMovies(BaseModel):
    title: str
    description: str
    year: int
    genre: str

class SUpdate(SMovies):
    title: str | None
    description: str | None
    year: int | None
    genre: str | None




