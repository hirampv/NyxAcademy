from django.shortcuts import render
from .models import Course


def login(request):
    return render(request, 'account/login.html')

def home(request):
    context = Course.objects.all()
    return render(request, 'home/home.html', {'context':context})

def youtube(request):
    return render(request, 'home/youtube.html')

def books(request):
    return render(request, 'home/books.html')

