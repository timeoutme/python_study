from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    miao_shu = Gallery.objects
    return render(request,'home.html',{'miao_shu':miao_shu})