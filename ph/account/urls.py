from django.urls import path
from .views import register_page, login

urlpatterns = [
    path('signup/', register_page,name='注册页面'),
    path('login/',login,name='登录页面'),
]