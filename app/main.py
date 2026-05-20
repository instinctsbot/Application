from fastapi import FastAPI
from app.config import settings
from app.api.router import api_router

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message" : "AI Store Monitor Running"
    }