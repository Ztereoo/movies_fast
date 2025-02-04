import asyncio
import json

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy import insert

from app.database import Base, async_session_maker, engine
from app.main import app as fastapi_app
from app.movies.models import Movie
from app.reviews.models import Review
from app.users.models import User
from config import MODE


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert MODE == 'TEST'
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock(model: str):
        with open(f'app/tests/mock_{model}.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    movies = open_mock("movies")
    users = open_mock("users")
    reviews = open_mock("reviews")

    async with async_session_maker() as session:
        add_movies = insert(Movie).values(movies)
        add_users = insert(User).values(users)
        add_reviews = insert(Review).values(reviews)

        await session.execute(add_movies)
        await session.execute(add_users)
        await session.execute(add_reviews)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield session






