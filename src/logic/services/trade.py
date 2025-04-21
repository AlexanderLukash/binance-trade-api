from dataclasses import dataclass

from src.infra.repositories.trade.base import BaseTradeRepository
from src.logic.services.base import BaseTradeService


@dataclass
class ORMTradeService(BaseTradeService):
    trade_repo: BaseTradeRepository

    async def get_prise_by_symbols(self, symbols: list[str]) -> list[int | float]:
        return await self.trade_repo.get_prise_by_symbols(symbols=symbols)

    async def get_stat_by_symbols(self, symbols: list[str]):
        return await self.trade_repo.get_stat_by_symbols(symbols)
