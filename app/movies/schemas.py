from pydantic import BaseModel, EmailStr

class SMovies(BaseModel):
    title: str
    description: str
    year: int
    genre: str