from fastapi.routing import APIRouter

from src.application.api.v2.trade.handlers import router as trade_router

router = APIRouter(
    prefix="/v2",
)

router.include_router(trade_router)
