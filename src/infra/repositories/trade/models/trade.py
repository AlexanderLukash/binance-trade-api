from tortoise import fields, models
from datetime import datetime


class TradeModel(models.Model):
    id = fields.BigIntField(pk=True)
    symbol = fields.CharField(max_length=20, index=True)
    trade_id = fields.BigIntField()
    price = fields.FloatField()
    quantity = fields.FloatField()
    is_buyer_market_maker = fields.BooleanField()
    created_at = fields.DatetimeField(default=datetime.now, index=True)

    class Meta:
        table = "trades"


class TradeStatModel(models.Model):
    symbol = fields.CharField(max_length=20, index=True, unique=True)
    min_price = fields.FloatField()
    max_price = fields.FloatField()
    avg_price = fields.FloatField()
    trades_count = fields.IntField(default=0)
    last_updated = fields.DatetimeField(default=datetime.now)

    class Meta:
        table = "trade_stats"
