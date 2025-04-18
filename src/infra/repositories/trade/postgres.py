from dataclasses import dataclass
import logging

from src.infra.repositories.trade.base import BaseTradeRepository
from src.infra.repositories.trade.models.trade import TradeModel

logger = logging.getLogger(__name__)


@dataclass
class PostgresTradeRepository(BaseTradeRepository):
    async def get_prise_by_symbols(self, symbols: list[str]) -> list[float | int]:
        prices = []

        for symbol in symbols:
            trade = (
                await TradeModel.filter(symbol=symbol).order_by("-created_at").first()
            )
            prices.append(trade.price if trade else None)

        return prices

    async def get_stat_by_symbols(self, symbols: list[str]): ...
