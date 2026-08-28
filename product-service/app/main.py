from fastapi import FastAPI

from .database import Base, engine
from . import models
from .routes import router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="ShopSphere Product Service"
)


app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Product Service is running"
    }