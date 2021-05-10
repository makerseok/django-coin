import requests


def namelist():
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails": "false"}
    response = requests.request("GET", url, params=querystring).json()
    NAMES = tuple((name['market'], name['korean_name']) for name in response)
    return NAMES


def namelist_split():
    result = {
        'KRW': [],
        'BTC': [],
        'USD': [],
    }
    for name in namelist():
        result[name[0][:3]].append(name)
    result['USDT'] = result['USD']
    del (result['USD'])
    return result


def get_coin_list(string):
    url = "https://api.upbit.com/v1/ticker"
    querystring = {"markets": string}
    response = requests.request("GET", url, params=querystring).json()
    return response


def update(response):
    from .models import CoinData
    if CoinData.objects.filter(market=response['market']).count() > 0:
        c = CoinData.objects.filter(market=response['market'])
        c.update(
            coin_name=response['market'],
            market=response['market'],
            high_price=response['high_price'],
            low_price=response['low_price'],
            trade_price=response['trade_price'],
            signed_change_price=response['signed_change_price'],
            signed_change_rate=round(response['signed_change_rate'] * 100, 2),
            acc_trade_volume_24h=response['acc_trade_volume_24h'],
            acc_trade_price_24h=response['acc_trade_price_24h']
        )
    else:
        CoinData.objects.create(
            coin_name=response['market'],
            market=response['market'],
            high_price=response['high_price'],
            low_price=response['low_price'],
            trade_price=response['trade_price'],
            signed_change_price=response['signed_change_price'],
            signed_change_rate=round(response['signed_change_rate'] * 100, 2),
            acc_trade_volume_24h=response['acc_trade_volume_24h'],
            acc_trade_price_24h=response['acc_trade_price_24h']
        )
