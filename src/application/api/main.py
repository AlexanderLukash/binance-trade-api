from contextlib import asynccontextmanager

from fastapi import FastAPI
from punq import Container
from tortoise.contrib.fastapi import register_tortoise

from src.application.api.middlewares.main import setup_middlewares
from src.application.api.v1.urls import router as v1_router
from src.logic.init import init_container
from src.settings.config import Config


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app():
    container: Container = init_container()
    config: Config = container.resolve(Config)
    app = FastAPI(
        title="Simple Bibance API",
        docs_url="/api/docs",
        description="A simple kafka + ddd example.",
        debug=True,
        lifespan=lifespan,
    )
    setup_middlewares(app)
    register_tortoise(
        app,
        db_url=config.database_url,
        modules={"models": ["src.infra.repositories.trade.models.trade"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
    app.include_router(v1_router, prefix="/api")

    return app
