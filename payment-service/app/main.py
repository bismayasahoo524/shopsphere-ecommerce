from fastapi import FastAPI

from .database import Base, engine
from . import models
from .routes import router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="ShopSphere Payment Service"
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "Payment Service is running"
    }