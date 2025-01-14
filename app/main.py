import uvicorn
from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def get_smth():
    return {"this is": "something"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)