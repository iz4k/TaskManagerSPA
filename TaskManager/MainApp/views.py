from django.shortcuts import render

def home(request):
    return render(request, 'MainApp/home.html')
# Create your views here.
