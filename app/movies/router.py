import time

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.movies.dao import Movies_Dao
from app.movies.schemas import SMovies, SUpdate

router = APIRouter(
    prefix='/movies',
    tags=['movies']
)


@router.get('')
@cache(expire=20)
async def get_movies() -> list[SMovies]:
    return await Movies_Dao.find_all()


@router.get('/{id}')
async def get_by_id(id: int) -> SMovies:
    return await Movies_Dao.find_by_id(id)


@router.delete('/{id}')
async def delete_item(id: int):
    return await Movies_Dao.delete_item(id)


@router.put('/{id}')
async def update_item(id: int, payload: SUpdate) -> SMovies:
    update_data = payload.dict()
    return await Movies_Dao.update(id, **update_data)


@router.post('')
async def add_item(data: SMovies):
    return await Movies_Dao.add_item(**data.dict())
