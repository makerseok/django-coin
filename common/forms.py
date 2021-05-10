from coin.ftns import influ
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserForm(UserCreationForm):
    """
    회원가입에 사용하기 위한 폼
    """
    email = forms.EmailField(label='이메일')
    namelist = forms.CharField(max_length=200, required=False)
    influencer_list = tuple((i, j) for i, j in zip(influ, influ))
    influencers = forms.CharField(max_length=50)

    class Meta:
        model = get_user_model()  # UserCreationForm 모델 클래스에 username, password 1, 2
        fields = ('username', 'email', 'namelist', 'influencers')


class CustomUserupdateForm(UserChangeForm):
    """
    회원정보수정에 사용하기 위한 폼
    """
    email = forms.EmailField(label='이메일')
    namelist = forms.CharField(max_length=200, required=False)
    influencer_list = tuple((i, j) for i, j in zip(influ, influ))
    influencers = forms.CharField(max_length=50)

    class Meta:
        model = get_user_model()  # UserCreationForm 모델 클래스에 username, password 1, 2
        fields = ('username', 'email', 'namelist', 'influencers')
