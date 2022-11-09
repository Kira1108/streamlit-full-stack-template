import uuid

from fastapi import FastAPI
from fastapi import Depends

from app import config
from app.config import Settings
from app.routers import example


app = FastAPI()

@app.get("/")
def index_url():
    return {"message": "Welcome to API"}
    


@app.get("/ping")
def ping(settings:Settings = Depends(config.get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }

app.include_router(example.router)