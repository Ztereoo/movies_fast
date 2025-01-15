from app.database import async_session_maker
from sqlalchemy import select, insert
from fastapi import HTTPException

class BaseDao():
    model= None

    @classmethod
    async def find_all(cls):
        if not cls.model:
            raise HTTPException(status_code=500, detail='No such model')

        async with async_session_maker() as session:
            stmt = select(cls.model)
            result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def find_by_id(cls,model_id: int):
        async with async_session_maker() as session:
            stmt= select(cls.model).filter_by(id=model_id)
            result= await session.execute(stmt)
            return result.scalars().one_or_none()


    @classmethod
    async def find_selected(cls,**data):
        async with async_session_maker() as session:
            stmt= select(cls.model).filter_by(**data)
            result = await session.execute(stmt)
            return result.scalar().one_or_none()

    @classmethod
    async def add_item(cls, **data):
        async with async_session_maker() as session:
            stmt= insert(cls.model).values(**data)
            result= await session.execute(stmt)
            await session.commit()
            return result






