from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.application.api.v1.urls import router as v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app():
    app = FastAPI(
        title="Simple Bibance API",
        docs_url="/api/docs",
        description="A simple kafka + ddd example.",
        debug=True,
        lifespan=lifespan,
    )
    app.include_router(v1_router, prefix="/api")

    return app
