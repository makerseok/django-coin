from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Twitters


@login_required(login_url='/common/login')
def index(request):
    current_user = request.user
    influencers = current_user.profile.influencers
    context = {
        'twitter_urls': influencers.split(","),
    }
    return render(request, 'twitter/index.html', context)


@login_required(login_url='/common/login')
def detail(request, target):
    target_twit = Twitters.objects.get(twit_name=target.split('-')[1])
    twitter_url = target_twit.get_twit_name_display()
    context = {
        'twitter_url': twitter_url,
    }

    return render(request, 'twitter/detail.html', context)
