from django.db import models


class CoinData(models.Model):
    from . import ftns
    coin_name = models.CharField(max_length=20, choices=ftns.namelist())  #
    market = models.CharField(max_length=20)  # ticker
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    signed_change_price = models.FloatField()
    signed_change_rate = models.FloatField()
    acc_trade_volume_24h = models.IntegerField()
    acc_trade_price_24h = models.IntegerField()

    def __str__(self):
        return self.market
