import logging

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from src.application.api.middlewares.context import set_request_id_middleware
from src.application.api.middlewares.structlog import structlog_bind_middleware


logger = logging.getLogger(__name__)


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(BaseHTTPMiddleware, dispatch=structlog_bind_middleware)
    app.add_middleware(BaseHTTPMiddleware, dispatch=set_request_id_middleware)
