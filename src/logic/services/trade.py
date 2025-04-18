from dataclasses import dataclass

from src.infra.repositories.trade.base import BaseTradeRepository
from src.logic.services.base import BaseTradeService


@dataclass
class ORMTradeService(BaseTradeService):
    trade_repo: BaseTradeRepository

    async def get_prise_by_symbols(self, symbols: list[str]) -> list[int | float]:
        return await self.trade_repo.get_prise_by_symbols(symbols=symbols)

    async def get_stat_by_symbols(self, symbols: list[str]):
        raw_stats = await self.trade_repo.get_stat_by_symbols(symbols)

        stats_map = {
            stat["symbol"]: {
                "min_price": float(stat["min_price"])
                if stat["min_price"] is not None
                else None,
                "max_price": float(stat["max_price"])
                if stat["max_price"] is not None
                else None,
                "avg_price": float(stat["avg_price"])
                if stat["avg_price"] is not None
                else None,
            }
            for stat in raw_stats
        }

        result = []
        for symbol in symbols:
            symbol_usdt = f"{symbol}USDT"
            if symbol_usdt in stats_map:
                result.append(
                    {
                        "symbol": symbol,
                        "min_price": stats_map[symbol_usdt]["min_price"],
                        "max_price": stats_map[symbol_usdt]["max_price"],
                        "avg_price": stats_map[symbol_usdt]["avg_price"],
                    },
                )
            else:
                result.append(
                    {
                        "symbol": symbol,
                        "min_price": None,
                        "max_price": None,
                        "avg_price": None,
                    },
                )

        return result
