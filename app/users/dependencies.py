from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError
from config import KEY, ALGORITHM
from datetime import datetime
from app.users.dao import UserDao

def get_token(request: Request):
    token= request.cookies.get('booking_access_token')
    if not token:
        return HTTPException(status_code=401,detail='No token')
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload= jwt.decode(
            token, KEY, ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=401, detail='No JWT token')

    expire= payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=401, detail='Token is not valid anymore')
    user_id= payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=401, detail='No id in payload')

    user= await UserDao.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=401, detail='No user')
    return user