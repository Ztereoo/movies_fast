from fastapi import APIRouter
from app.movies.models import Movie
from app.database import async_session_maker
from sqlalchemy import select, insert
from app.movies.schemas import SMovies

router= APIRouter(
    prefix='/movies',
    tags=['movies']
)

@router.get('')
async def get_movies():
    async with async_session_maker() as session:
        stmt= select(Movie)
        result= await session.execute(stmt)
        movies= result.scalars().all()
        return movies

@router.post('')
async def add_movies(data: SMovies):
    async with async_session_maker() as session:
        stmt= insert(Movie).values(**data.dict())
        await session.execute(stmt)
        await session.commit()

