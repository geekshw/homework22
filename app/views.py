from django.shortcuts import render
from .models import Banner
def app(request):
    return render(request , 'index.html')

def banner_list(request):
    banners = Banner.objects.all() 
    return render(request, 'banner_list.html', {'banners': banners})


