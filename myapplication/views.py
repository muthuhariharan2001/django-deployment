from django.shortcuts import render


def function1(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')
