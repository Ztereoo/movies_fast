import uvicorn
from fastapi import FastAPI
from app.movies.router import router as router_movies
from app.users.router import router as router_users

app= FastAPI()


app.include_router(router_movies)
app.include_router(router_users)

if __name__ == "__main__":
    uvicorn.run(app)