import os
from datetime import datetime, timedelta

from fastapi import Depends
from dotenv import load_dotenv
from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from sqlalchemy.ext.asyncio import AsyncSession

from app.users.dao import UserDao
from app.database import get_session

load_dotenv()

ALGORITHM = os.getenv("ALGORITHM")
KEY = os.getenv("KEY")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        KEY,
        ALGORITHM,
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str, session: AsyncSession = Depends(get_session)):
    user = await UserDao.find_selected(session, email=email)
    if not user:
        raise HTTPException(status_code=401, detail="No such user")
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return user
