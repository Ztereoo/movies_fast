import os
from urllib.parse import urlparse

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

MODE = os.getenv("MODE", "DEV")

DATABASE_URL = "sqlite+aiosqlite:///movies.db"

DATABASE_TEST_URL = "sqlite+aiosqlite:///test_movies.db"

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgres+asyncpg://")

if MODE == "TEST":
    DATABASE_URL = DATABASE_TEST_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = DATABASE_URL
    DATABASE_PARAMS = {}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = async_sessionmaker(
    bind=engine, autoflush=False, expire_on_commit=False, autocommit=False
)


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass
