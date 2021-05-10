from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from . import ftns
from .models import CoinData


@login_required(login_url='/common/login')
def index(request):
    target_coins = update(request)
    context = {
        'coin_data': [CoinData.objects.get(market=target_coin) for target_coin in target_coins.split(",")],
        'target_coin': CoinData.objects.get(market=target_coins.split(",")[0]),
    }

    context = {
        'coin_data': [CoinData.objects.get(market=target_coin) for target_coin in target_coins.split(",")],
        'target_coin': CoinData.objects.get(market=target_coins.split(",")[0]),
    }
    return render(request, 'coin/coin.html', context)


@login_required(login_url='/common/login')
def update(request):
    current_user = request.user
    target_coins = current_user.profile.namelist
    responses = ftns.get_coin_list(target_coins)
    for response in responses:
        ftns.update(response)
    return target_coins


@login_required(login_url='/common/login')
def refresh_list(request):
    target_coins = update(request)
    print(target_coins)
    context = {
        'coin_data': [CoinData.objects.get(market="KRW-ETC")],
    }
    return render(request, 'coin/list.html', context)


def detail(request, target):
    context = {
        'target_coin': CoinData.objects.get(market=target),
    }
    return render(request, 'coin/detail.html', context)


def get_by_ajax(request):
    target_coin = request.POST.get('target_coin')[1:-1]
    context = {'target_coin': target_coin}
    return JsonResponse(context)
