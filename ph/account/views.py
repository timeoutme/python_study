from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def register_page(request):
    if request.method == 'GET':
        return render(request,'register_page.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        password2 = request.POST['确认密码']   
        try:
            User.objects.get(username=user_name)
            return render(request,'register_page.html',{'用户名错误':'改用户名已存在'})
        except User.DoesNotExist:
            if password1 == password2:
                User.objects.create_user(username=user_name,password=password1)
                return redirect('主页')
            else:
                return render(request,'register_page.html',{'密码错误':'两次输入的密码不一致'})       
    

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')   
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        user = auth.authenticate(username=user_name,password=password1)
        if user == None:
            return render(request,'login.html', {'错误':'用户名或密码错误'})
        else:
            auth.login(request,user)
            return redirect('主页')         