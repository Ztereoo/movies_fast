import uvicorn
from fastapi import FastAPI,Depends
from app.movies.router import router as router_movies
from app.users.router import router as router_users
from app.reviews.router import router as router_reviews
from app.users.models import User
from app.users.dependencies import get_current_user
from dao.base import BaseDao

app= FastAPI()


app.include_router(router_movies)
app.include_router(router_users)
app.include_router(router_reviews)

# @app.get('/rev')
# async def get_reviews(user: User= Depends(get_current_user)):
#     print(user, type(user), user.email)



if __name__ == "__main__":
    uvicorn.run(app)