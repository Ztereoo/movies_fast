from fastapi import HTTPException
from sqlalchemy import insert, select, and_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.logger import logger


class BaseDao:
    model = None

    @classmethod
    async def find_all(cls, session: AsyncSession, **filter_by):
        if not cls.model:
            raise HTTPException(status_code=500, detail="No such model")

        stmt = select(cls.model).filter_by(**filter_by)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_by_id(cls, model_id: int, session: AsyncSession):
        try:
            stmt = select(cls.model).filter_by(id=model_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database exc: cannot execute data"
            else:
                msg = f"Unknown error {e} no data"
            logger.error(msg, exc_info=True)

    @classmethod
    async def find_selected(cls, session: AsyncSession, **data):
        stmt = select(cls.model).filter(and_(*(getattr(cls.model, key) == value
                                               for key, value in data.items())))
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def add_item(cls, session: AsyncSession, **data):
        new_obj = cls.model(**data)
        session.add(new_obj)
        await session.commit()
        await session.refresh(new_obj)
        return new_obj

    @classmethod
    async def add_csv_data(cls, movies, session: AsyncSession):
        session.add_all(movies)
        await session.commit()

    @classmethod
    async def update(cls, model_id, session: AsyncSession, **kwargs):
        stmt = select(cls.model).filter(cls.model.id == model_id)
        result = await session.execute(stmt)
        item = result.scalars().one_or_none()
        if not item:
            raise HTTPException(status_code=400, detail="No such item")
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
            else:
                raise HTTPException(status_code=400, detail="No such key")
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

    @classmethod
    async def delete_item(cls, model_id, session: AsyncSession):
        stmt = select(cls.model).filter_by(id=model_id)
        item = await session.execute(stmt)
        item = item.scalars().one_or_none()
        if item:
                await session.delete(item)
                await session.commit()
                return f"Item deleted"
        return HTTPException(status_code=400, detail="no item with such id")
