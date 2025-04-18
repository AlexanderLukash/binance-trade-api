from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseTradeRepository(ABC):
    @abstractmethod
    async def get_prise_by_symbols(self, symbols: list[str]) -> list[float | int]: ...

    @abstractmethod
    async def get_stat_by_symbols(self, symbols: list[str]): ...
