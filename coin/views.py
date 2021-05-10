from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from . import ftns
from .models import CoinData


@login_required(login_url='/common/login')
def index(request):
    """
    detail 페이지 첫 화면
    """
    target_coins = update(request)
    context = {
        'coin_data': [CoinData.objects.get(market=target_coin) for target_coin in target_coins.split(",")],
        'target_coin': CoinData.objects.get(market=target_coins.split(",")[0]),
    }
    return render(request, 'coin/coin.html', context)


@login_required(login_url='/common/login')
def update(request):
    """
    사용자가 설정한 암호화폐의 정보를 upbit api를 사용해 업데이트 후 db에 저장
    사용자의 암호화폐 리스트를 문자열로 반환
    """
    current_user = request.user
    target_coins = current_user.profile.namelist
    responses = ftns.get_coin_list(target_coins)
    for response in responses:
        ftns.update(response)
    return target_coins


@login_required(login_url='/common/login')
def refresh_list(request):
    """
    리스트 새로고침 하고싶었지만 실패~
    사용 x
    """
    target_coins = update(request)
    print(target_coins)
    context = {
        'coin_data': [CoinData.objects.get(market="KRW-ETC")],
    }
    return render(request, 'coin/list.html', context)


def detail(request, target):
    """
    인수로 받은 암호화폐의 정보를 detail.html에 반환
    ajax 사용
    """
    context = {
        'target_coin': CoinData.objects.get(market=target),
    }
    return render(request, 'coin/detail.html', context)


def get_by_ajax(request):
    """
    ajax 통신 시 호출해 json 형식 target_coin 반환
    """
    target_coin = request.POST.get('target_coin')[1:-1]
    context = {'target_coin': target_coin}
    return JsonResponse(context)
