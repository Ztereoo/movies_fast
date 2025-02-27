import time
from contextlib import asynccontextmanager
from datetime import datetime

import uvicorn
from app.database import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin
from app.logger import logger

from app.admin.views import MovieAdmin, ReviewAdmin, UserAdmin
from app.images.router import router as router_images
from app.movies.router import router as router_movies
from app.reviews.router import router as router_reviews
from app.users.router import router as router_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")

    yield
    await redis.close()


app = FastAPI(lifespan=lifespan)

admin = Admin(app, engine)

admin.add_view(UserAdmin)
admin.add_view(MovieAdmin)
admin.add_view(ReviewAdmin)

app.mount("/static", StaticFiles(directory="app/static"), "static")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request execution time", extra={
        "process_time": round(process_time, 4)
    })
    return response


app.include_router(router_movies)
app.include_router(router_users)
app.include_router(router_reviews)
app.include_router(router_images)

# if __name__ == "__main__":
#     uvicorn.run(app)
