from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all(request):
    return render(request, 'all.html')

def new(request):
    return render(request, 'new.html')

def play(request):
    return render(request, 'play.html')

def best(request):
    return render(request, 'best.html')

def category(request):
    return render(request, 'category.html')