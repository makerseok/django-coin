from coin.ftns import influ
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from coin import ftns
from .forms import UserForm, CustomUserupdateForm


def signup(request):
    INFLUENCER_LIST = influ
    NAMELIST = ftns.namelist()
    namelist_dic = ftns.namelist_split()
    context = {
        'NAMELIST': NAMELIST,
        'INFLUENCER_LIST': INFLUENCER_LIST,
        'NAMELIST_KRW': namelist_dic['KRW'],
        'NAMELIST_BTC': namelist_dic['BTC'],
        'NAMELIST_USDT': namelist_dic['USDT'],
    }
    if request.method == "POST":
        form = UserForm(request.POST)
        print(request.POST.getlist('namelist'))
        if form.is_valid() and request.POST.getlist('namelist') != "":
            user = form.save()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.namelist = ",".join(request.POST.getlist('namelist'))
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('coin:index')
        else:
            context['form'] = form
            return render(request, 'common/signup.html', context=context)
    else:
        form = UserForm()
        context['form'] = form
        return render(request, 'common/signup.html', context=context)


def update(request):
    INFLUENCER_LIST = influ
    NAMELIST = ftns.namelist()
    namelist_dic = ftns.namelist_split()
    context = {
        'NAMELIST': NAMELIST,
        'INFLUENCER_LIST': INFLUENCER_LIST,
        'NAMELIST_KRW': namelist_dic['KRW'],
        'NAMELIST_BTC': namelist_dic['BTC'],
        'NAMELIST_USDT': namelist_dic['USDT'],
    }
    if request.method == "POST":
        form = CustomUserupdateForm(request.POST, instance=request.user)
        if form.is_valid() and request.POST.getlist('namelist'):
            user = request.user
            user.profile.namelist = ",".join(request.POST.getlist('namelist'))
            user.profile.influencers = ",".join(request.POST.getlist('influencers'))
            user.save()
            return redirect('coin:index')
        
        else:
            if not request.POST.getlist('namelist'):
                context['form'] = form
                context['errormsg'] = '하나 이상의 종목을 선택해야 합니다'
                return render(request, 'common/update.html', context=context)

            elif not request.POST.getlist('influencers'):
                context['form'] = form
                context['errormsg'] = '한 명 이상의 인플루언서를 선택해야 합니다'
                return render(request, 'common/update.html', context=context)
    else:
        form = CustomUserupdateForm()
        context['form'] = form
        return render(request, 'common/update.html', context=context)
