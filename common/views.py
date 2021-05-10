from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from coin import ftns
from .forms import UserForm, CustomUserupdateForm


def signup(request):
    NAMELIST = ftns.namelist()
    namelist_dic = ftns.namelist_split()
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
            context = {
                'NAMELIST': NAMELIST,
                'form': form,
                'NAMELIST_KRW': namelist_dic['KRW'],
                'NAMELIST_BTC': namelist_dic['BTC'],
                'NAMELIST_USDT': namelist_dic['USDT'],
            }
            return render(request, 'common/signup.html', context=context)
    else:
        form = UserForm()
        context = {
            'NAMELIST': NAMELIST,
            'form': form,
            'NAMELIST_KRW': namelist_dic['KRW'],
            'NAMELIST_BTC': namelist_dic['BTC'],
            'NAMELIST_USDT': namelist_dic['USDT'],
        }
        return render(request, 'common/signup.html', context=context)


def update(request):
    NAMELIST = ftns.namelist()
    namelist_dic = ftns.namelist_split()
    if request.method == "POST":
        form = CustomUserupdateForm(request.POST, instance=request.user)
        if form.is_valid() and request.POST.getlist('namelist'):
            user = request.user
            user.profile.namelist = ",".join(request.POST.getlist('namelist'))
            user.save()
            return redirect('coin:index')
        elif not request.POST.getlist('namelist'):
            context = {
                'NAMELIST': NAMELIST,
                'form': form,
                'NAMELIST_KRW': namelist_dic['KRW'],
                'NAMELIST_BTC': namelist_dic['BTC'],
                'NAMELIST_USDT': namelist_dic['USDT'],
                'errormsg': "하나 이상의 종목을 선택해야 합니다.",
            }
            return render(request, 'common/update.html', context=context)
    else:
        form = CustomUserupdateForm()
        context = {
            'NAMELIST': NAMELIST,
            'form': form,
            'NAMELIST_KRW': namelist_dic['KRW'],
            'NAMELIST_BTC': namelist_dic['BTC'],
            'NAMELIST_USDT': namelist_dic['USDT'],
        }
        return render(request, 'common/update.html', context=context)
