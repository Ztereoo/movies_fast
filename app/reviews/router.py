from fastapi import APIRouter, Depends

from app.reviews.dao import ReviewDao
from app.users.dependencies import get_current_user
from app.users.models import User

router = APIRouter(
    prefix='/reviews',
    tags=['Reviews'],
)

@router.get('/all_reviews')
async def get_all_reviews():
    return await ReviewDao.find_all()

@router.get('/get_users_reviews')
async def get_users_reviews(user: User= Depends(get_current_user)):
    return await ReviewDao.find_all(user_id=user.id)





