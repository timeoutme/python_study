from django.urls import path
from .views import publish

urlpatterns = [
    path('publish/', publish, name='产品发布页面'),
]
