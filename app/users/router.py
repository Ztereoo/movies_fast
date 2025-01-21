from fastapi import APIRouter, HTTPException, Response
from app.users.schemas import SUserRegister, SUSerLogin
from app.users.dao import UserDao
from app.users.auth import get_password_hash
from app.users.auth import authenticate_user, create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post('/registration')
async def registration(user_data: SUserRegister):
    existing_user = await UserDao.find_selected(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=401, detail='user already exist')
    hashed_password = get_password_hash(user_data.password)
    await UserDao.add_item(email=user_data.email, name=user_data.name, hashed_password=hashed_password)


@router.post('/login')
async def login(response: Response, user_data: SUSerLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='No such user')
    token = create_access_token({'sub': str(user.id)})
    response.set_cookie("booking_access_token", token, httponly=True)
    return token
