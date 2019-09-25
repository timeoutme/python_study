from django.urls import path
from .views import publish, products_list, product_detail

urlpatterns = [
    path('publish/', publish, name='产品发布页面'),
    
    path('products_list',products_list,name='产品列表页面'),
    path('<int:product_id>',product_detail, name='产品详情页面'),
]
