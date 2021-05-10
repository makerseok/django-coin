import random

from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup
from coin.models import CoinData


def index(request):
    url = 'https://kr.coinness.com'
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')

    titles = bs.select("div > a > h3")
    texts = bs.select(".h63")

    coinness = []

    for title, text, link in zip(titles, texts, titles):
        coinness.append((
            " ".join(title.get_text().split()[1:]),
            text.get_text(),
            url + link.parent.get('href')
        ))

    url = 'https://www.coindeskkorea.com/news/articleList.html?view_type=sm'
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')

    titles = bs.select(".list-titles > a")
    texts = bs.select(".list-summary > a.line-height-4-2x")

    coindeskkorea = []

    for title, text, link in zip(titles, texts, titles):
        coindeskkorea.append((
            " ".join(title.get_text().split()[1:]),
            text.get_text(),
            url.split("/news")[0] + link.get('href')
        ))

    url = 'https://www.tokenpost.kr/articles'
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')

    titles = bs.select(".articleListTitle.marginB8 > a")
    texts = bs.select(".articleListCont")

    tokenpost = []

    for title, text, link in zip(titles, texts, titles):
        tokenpost.append((
            " ".join(title.get_text().split()[1:]),
            text.get_text(),
            url.split("/articles")[0] + link.get('href')
        ))

    df = pd.read_csv("static/data.csv", sep="|")

    word = [(v['word'], v['content']) for k, v in df.iterrows()]
    context = {
        'coinness': coinness,
        'coindeskkorea': coindeskkorea,
        'tokenpost': tokenpost,
        'word': random.choice(word),
    }

    return render(request, 'article/index.html', context)


def get_news(request, target):
    if request.is_ajax():
        target_name = CoinData.objects.get(coin_name=target).get_coin_name_display()
    else:
        current_user = request.user
        target_coins = current_user.profile.namelist
        target = target_coins.split(",")[0]
        target_name = CoinData.objects.filter(coin_name=target).get_coin_name_display()

    url = f"https://search.naver.com/search.naver?query={target_name}&where=news&ie=utf8&sm=nws_hty"
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')

    titles = bs.select(".news_tit")
    texts = bs.select(".api_txt_lines.dsc_txt_wrap")
    result = []
    for title, text, link in zip(titles, texts, titles):
        result.append((
            title.get_text(),
            text.get_text(),
            link.get('href')
        ))

    context = {
        'articles': result
    }
    return render(request, 'article/detail.html', context)
