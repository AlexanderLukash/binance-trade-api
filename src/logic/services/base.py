from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseTradeService(ABC):
    @abstractmethod
    async def get_prise_by_symbols(self, symbols: list[str]) -> list[int | float]: ...

    @abstractmethod
    async def get_stat_by_symbols(self, symbols: list[str]): ...
