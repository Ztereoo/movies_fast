import uvicorn
from fastapi import FastAPI
from app.movies.router import router as router_movies

app= FastAPI()

@app.get('/')
def get_smth():
    return {"this is": "something"}

app.include_router(router_movies)

if __name__ == "__main__":
    uvicorn.run(app)