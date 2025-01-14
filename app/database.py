from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL= "sqlite+aiosqlite:///movies.db"

engine= create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass