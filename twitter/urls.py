from django.urls import path, re_path
from . import views

app_name = 'twitter'

urlpatterns = [
    path('<str:target>', views.detail, name='detail'),
    path('', views.index, name='index'),
]
