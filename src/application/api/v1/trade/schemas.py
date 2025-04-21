from typing import Optional

from pydantic import BaseModel, Field


class PriseRequestSchema(BaseModel):
    symbols: list[str] = Field(..., examples=[["BTC", "ETH"]])


class PriceResponseSchema(BaseModel):
    prices: dict[str, float | int]


class StatsResponseSchema(BaseModel):
    symbol: str
    min_price: Optional[float | int]
    max_price: Optional[float | int]
    avg_price: Optional[float | int]
    trades: Optional[int]
