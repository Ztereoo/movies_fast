from passlib.context import CryptContext
from fastapi import HTTPException
# import jwt
from jose import jwt
from datetime import datetime, timedelta
from app.users.dao import UserDao
from pydantic import EmailStr
from config import KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode,
        KEY,
        ALGORITHM,
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UserDao.find_selected(email=email)
    if not user:
        raise HTTPException(status_code=401, detail='No such user')
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Incorrect password')
    return user

