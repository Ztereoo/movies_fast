from fastapi import APIRouter
from app.movies.models import Movie
from app.database import async_session_maker
from sqlalchemy import select, insert
from app.movies.schemas import SMovies
from app.movies.dao import Movies_Dao

router= APIRouter(
    prefix='/movies',
    tags=['movies']
)

# @router.get('')
# async def get_movies():
#
#     async with async_session_maker() as session:
#         stmt= select(Movie)
#         result= await session.execute(stmt)
#         movies= result.scalars().all()
#         return movies
@router.get('')
async def get_movies():
    return await Movies_Dao.find_all()

@router.get('/{id}')
async def get_by_id(id):
    return await Movies_Dao.find_by_id(id)

# @router.get('by_id/{id}')
# async def get_movie_by_id(id):
#     async with async_session_maker() as session:
#         stmt= select(Movie).filter_by(id=id)
#         res= await session.execute(stmt)
#         return res.scalar_one_or_none()

@router.post('')
async def add_movies(data: SMovies):
    async with async_session_maker() as session:
        stmt= insert(Movie).values(**data.dict())
        await session.execute(stmt)
        await session.commit()

