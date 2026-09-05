from fastapi import FastAPI

from .database import Base, engine
from .routes import router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="ShopSphere Order Service"
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "Order Service is running"
    }