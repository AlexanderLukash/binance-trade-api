from tortoise import fields, models
from datetime import datetime
import uuid


class TradeModel(models.Model):
    oid = fields.CharField(max_length=36, pk=True, default=str(uuid.uuid4))
    symbol = fields.CharField(max_length=20, index=True)
    trade_id = fields.BigIntField()
    price = fields.FloatField()
    quantity = fields.FloatField()
    is_buyer_market_maker = fields.BooleanField()
    created_at = fields.DatetimeField(default=datetime.now)

    class Meta:
        table = "trades"
