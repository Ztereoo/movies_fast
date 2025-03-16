from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from app.reviews.dao import ReviewDao
from app.users.dependencies import get_current_user
from app.users.models import User
from app.database import get_session

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"],
)


@router.get("/all_reviews")
async def get_all_reviews(session: AsyncSession = Depends(get_session)):
    return await ReviewDao.find_all(session)


@router.get("/get_users_reviews")
async def get_users_reviews(user: User = Depends(get_current_user),
                            session: AsyncSession = Depends(get_session)):
    return await ReviewDao.find_all(session,user_id=user.id)
