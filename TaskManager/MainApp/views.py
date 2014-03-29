from django.shortcuts import render
from django.template import RequestContext

def home(request):
    return render(request, 'MainApp/home.html')

def login(request):
    return render(request, 'MainApp/login.html')
