from django.shortcuts import render, redirect
from .models import Products
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def publish(request):
    if request.method == 'GET':    
        return render(request,'publish.html')
    elif request.method == 'POST':
        product_name = request.POST['产品名称']
        product_intro = request.POST['简介']
        product_url = request.POST['产品链接']
        try:
            product_icon = request.FILES['图标']
            product_image = request.FILES['产品大图']
            product = Products()
            
            product.title = product_name
            product.intro = product_intro
            product.product_url = product_url
            product.product_icon = product_icon
            product.product_image = product_image
            product.publish_date = timezone.datetime.now()
            product.hunter = request.user    
            product.save()
            return redirect('主页') 
        except Exception as err:
            return render(request,'publish.html',{'错误':err})
        
        

        