from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def youtube(request):
    return render(request, 'home/youtube.html')

def books(request):
    return render(request, 'home/books.html')