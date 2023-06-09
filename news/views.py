from django.shortcuts import render
import requests
# Create your views here.

def news(request):
    return render(request, 'news.html', locals())