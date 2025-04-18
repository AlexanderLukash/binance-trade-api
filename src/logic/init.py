from functools import lru_cache

from punq import Container, Scope

from src.infra.repositories.trade.base import BaseTradeRepository
from src.infra.repositories.trade.postgres import PostgresTradeRepository
from src.logic.services.base import BaseTradeService
from src.logic.services.trade import ORMTradeService
from src.settings.config import Config


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(Config, instance=Config(), scope=Scope.singleton)

    config: Config = container.resolve(Config)  # noqa

    container.register(BaseTradeRepository, PostgresTradeRepository)

    def init_trade_service() -> BaseTradeService:
        trade_repo = container.resolve(BaseTradeRepository)
        return ORMTradeService(trade_repo=trade_repo)

    container.register(
        BaseTradeService,
        factory=init_trade_service,
        scope=Scope.singleton,
    )
    return container
