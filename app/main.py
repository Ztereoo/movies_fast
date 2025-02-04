from contextlib import asynccontextmanager

import uvicorn
from database import engine
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from sqladmin import Admin, ModelView

from app.admin.views import MovieAdmin, ReviewAdmin, UserAdmin
from app.images.router import router as router_images
from app.movies.router import router as router_movies
from app.reviews.router import router as router_reviews
from app.users.models import User
from app.users.router import router as router_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")

    yield
    await redis.close()

app = FastAPI(lifespan=lifespan)

admin=Admin(app,engine)


admin.add_view(UserAdmin)
admin.add_view(MovieAdmin)
admin.add_view(ReviewAdmin)

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_movies)
app.include_router(router_users)
app.include_router(router_reviews)
app.include_router(router_images)


# @app.on_event('startup')
# async def startup():
#     redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="cache")



if __name__ == "__main__":
    uvicorn.run(app)
