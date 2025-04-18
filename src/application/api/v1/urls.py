from fastapi.routing import APIRouter

from src.application.api.v1.trade.handlers import router as trade_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(trade_router)
