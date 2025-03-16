import csv
from io import StringIO

from fastapi import APIRouter, File, HTTPException, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

from app.movies.dao import Movies_Dao
from app.movies.models import Movie
from app.movies.schemas import SMovies, SUpdate
from app.database import get_session

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("")
@cache(expire=20)
async def get_movies(session: AsyncSession = Depends(get_session)) -> list[SMovies]:
    return await Movies_Dao.find_all(session)


@router.get("/{id}")
async def get_by_id(id: int, session: AsyncSession = Depends(get_session)) -> SMovies:
    return await Movies_Dao.find_by_id(id, session)


@router.delete("/{id}")
async def delete_item(id: int, session: AsyncSession = Depends(get_session)):
    return await Movies_Dao.delete_item(id, session)


@router.put("/{id}")
async def update_item(id: int, payload: SUpdate, session: AsyncSession = Depends(get_session)) -> SMovies:
    update_data = payload.dict()
    return await Movies_Dao.update(id, session, **update_data)


@router.post("")
async def add_item(data: SMovies, session: AsyncSession = Depends(get_session)):
    return await Movies_Dao.add_item(session, **data.dict())


@router.post("/add_from_file")
async def add_from_file(file: UploadFile = File(...), session: AsyncSession = Depends(get_session)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Not CSV file")

    content = await file.read()
    csv_file = StringIO(content.decode("utf-8"))
    csv_reader = csv.reader(csv_file)

    next(csv_reader, None)

    movies = []
    for row in csv_reader:
        if len(row) < 4:
            continue
        title, description, year, genre = row
        movie = Movie(title=title, description=description, year=int(year), genre=genre)
        movies.append(movie)
    if not movies:
        raise HTTPException(status_code=400, detail="No data to add from CSV")
    await Movies_Dao.add_csv_data(movies, session)
    return f"Movies successfully added to db"
