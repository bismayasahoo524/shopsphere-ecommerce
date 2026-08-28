from fastapi import FastAPI

from .routes import router


app = FastAPI(
    title="ShopSphere Notification Service",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Notification Service is running"
    }