from django.http import JsonResponse
from django.shortcuts import render

from . import ftns
from .models import CoinData


def index(request):
    current_user = request.user
    target_coins = current_user.profile.namelist
    responses = ftns.get_coin_list(target_coins)
    for response in responses:
        ftns.update(response)

    context = {
        'coin_data': [CoinData.objects.filter(market=target_coin) for target_coin in target_coins.split(",")],
        'target_coin': CoinData.objects.get(market=target_coins.split(",")[0]),
    }
    return render(request, 'coin/coin.html', context)


def detail(request, target):
    context = {
        'target_coin': CoinData.objects.get(market=target),
    }
    return render(request, 'coin/detail.html', context)


def twitter(request, target):
    twitter_url = 'https://twitter.com/' + "elonmusk"
    context = {
        'twitter_url': twitter_url,
    }
    return render(request, 'coin/twitter.html', context)


def get_by_ajax(request):
    target_coin = request.POST.get('target_coin')[1:-1]
    context = {'target_coin': target_coin}
    return JsonResponse(context)
