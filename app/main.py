import uvicorn
from fastapi import FastAPI,Depends
from app.movies.router import router as router_movies
from app.users.router import router as router_users
from app.reviews.router import router as router_reviews
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

app= FastAPI()


app.include_router(router_movies)
app.include_router(router_users)
app.include_router(router_reviews)

@app.on_event('startup')
async def startup():
    redis= aioredis.from_url("redis://localhost", encoding="utf-8",decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")




if __name__ == "__main__":
    uvicorn.run(app)