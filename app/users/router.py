from fastapi import APIRouter, HTTPException, Response, Depends

from app.users.models import User
from app.users.schemas import SUserRegister, SUSerLogin
from app.users.dao import UserDao
from app.users.auth import get_password_hash
from app.users.auth import authenticate_user, create_access_token
from app.users.dependencies import get_current_user
from app.tasks.tasks import send_confirmation_to_registered_user

from pydantic import parse_obj_as

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
    user= await UserDao.add_item(email=user_data.email, name=user_data.name, hashed_password=hashed_password)
    user_dict = {
        "email": user.email,
        "name": user.name,
        "hashed_password": user.hashed_password
    }
    send_confirmation_to_registered_user.delay(user_dict, user_dict['email'])
    return user_dict


@router.post('/login')
async def login(response: Response, user_data: SUSerLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='No such user')
    token = create_access_token({'sub': str(user.id)})
    response.set_cookie("booking_access_token", token, httponly=True)
    return user

@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return f'User successfully logout'

@router.get('/me')
async def user_info(user: User= Depends(get_current_user)):
    return user


