from dataclasses import dataclass
import logging
from datetime import datetime, timedelta

from tortoise.functions import Min, Max, Avg

from src.infra.repositories.trade.base import BaseTradeRepository
from src.infra.repositories.trade.models.trade import TradeModel

logger = logging.getLogger(__name__)


@dataclass
class PostgresTradeRepository(BaseTradeRepository):
    async def get_prise_by_symbols(self, symbols: list[str]) -> list[float | int]:
        prices = []

        for symbol in symbols:
            trade = (
                await TradeModel.filter(symbol=f"{symbol}USDT")
                .order_by("-created_at")
                .first()
            )
            prices.append(trade.price if trade else None)

        return prices

    async def get_stat_by_symbols(self, symbols: list[str]) -> list[dict]:
        time_threshold = datetime.now() - timedelta(hours=24)
        symbol_usdt_list = [f"{symbol}USDT" for symbol in symbols]

        results = (
            await TradeModel.filter(
                symbol__in=symbol_usdt_list,
                created_at__gte=time_threshold,
            )
            .annotate(
                min_price=Min("price"),
                max_price=Max("price"),
                avg_price=Avg("price"),
            )
            .group_by("symbol")
            .values("symbol", "min_price", "max_price", "avg_price")
        )

        return results
