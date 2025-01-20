from fastapi import APIRouter
from app.movies.models import Movie
from app.database import async_session_maker
from sqlalchemy import select, insert
from app.movies.schemas import SMovies, SUpdate
from app.movies.dao import Movies_Dao

router = APIRouter(
    prefix='/movies',
    tags=['movies']
)

@router.get('')
async def get_movies():
    return await Movies_Dao.find_all()


@router.get('/{id}')
async def get_by_id(id):
    return await Movies_Dao.find_by_id(id)


@router.delete('/{id}')
async def delete_item(id):
    return await Movies_Dao.delete_item(id)


@router.put('/{id}')
async def update_item(id, payload:SUpdate):
    update_data = payload.dict()
    return await Movies_Dao.update(id, **update_data)


@router.post('')
async def add_item(data:SMovies):
    return await Movies_Dao.add_item(**data.dict())