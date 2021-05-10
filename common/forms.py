from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    namelist = forms.CharField(max_length=200, required=False)

    class Meta:
        model = get_user_model()  # UserCreationForm 모델 클래스에 username, password 1, 2
        fields = ('username', 'email', 'namelist')


class CustomUserupdateForm(UserChangeForm):
    email = forms.EmailField(label='이메일')
    namelist = forms.CharField(max_length=200, required=False)

    class Meta:
        model = get_user_model()  # UserCreationForm 모델 클래스에 username, password 1, 2
        fields = ('username', 'email', 'namelist')