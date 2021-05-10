from django.db import models


class Twitters(models.Model):
    """
    코인별 트위터 아이디 매핑해 저장
    """
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
