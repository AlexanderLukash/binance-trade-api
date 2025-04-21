from fastapi import APIRouter, Depends
from punq import Container

from src.application.api.v1.trade.schemas import (
    PriseRequestSchema,
    PriceResponseSchema,
    StatsResponseSchema,
)
from src.logic.init import init_container
from src.logic.services.base import BaseTradeService

router = APIRouter(
    prefix="/trades",
    tags=["Trades"],
)


@router.post("/prices", response_model=PriceResponseSchema)
async def get_prices(
    payload: PriseRequestSchema,
    container: Container = Depends(init_container),
):
    trade_service: BaseTradeService = container.resolve(BaseTradeService)
    raw_prices = await trade_service.get_prise_by_symbols(symbols=payload.symbols)
    prices = dict(zip(payload.symbols, raw_prices))
    return PriceResponseSchema(prices=prices)


@router.post("/stats", response_model=list[StatsResponseSchema])
async def get_stats(
    payload: PriseRequestSchema,
    container: Container = Depends(init_container),
):
    trade_service: BaseTradeService = container.resolve(BaseTradeService)
    stats = await trade_service.get_stat_by_symbols(payload.symbols)
    return [
        StatsResponseSchema(
            symbol=stat["symbol"],
            max_price=stat["max_price"],
            min_price=stat["min_price"],
            avg_price=stat["avg_price"],
            trades=stat["trades_count"],
        )
        for stat in stats
    ]
