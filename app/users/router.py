from fastapi import APIRouter,HTTPException
from app.users.schemas import SUserRegister
from app.users.dao import UserDao
from app.users.auth import get_password_hash

router= APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/registration')
async def registration(user_data:SUserRegister):
    existing_user= await UserDao.find_selected(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code='401', detail='user already exist')
    hashed_password= get_password_hash(user_data.password)
    await UserDao.add_item(email= user_data.email, name=user_data.name, hashed_password=hashed_password)

@router.get('/all_users')
async def get_all_users():
    await UserDao.find_all()

@router.get('')
async def login():
    pass