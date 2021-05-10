from django.db import models


class Twitters(models.Model):
    coin_list = (
        ('ETH', 'ethereum'),
        ('BTC', 'Bitcoin'),
        ('NEO', 'Neo_Blockchain'),
        ('MTL', 'metalpaysme'),
        ('LTC', 'litecoin'),
        ('XRP', 'Ripple'),
        ('ETC', 'eth_classic'),
        ('OMG', 'omgnetworkhq'),
    )
    twit_name = models.CharField(max_length=20, choices=coin_list)  #
