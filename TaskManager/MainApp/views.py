from django.shortcuts import render

def home(request):
    return render(request, 'MainApp/home.html')
    
# THIS IS DONE IN LOGIN MODULE NOW
# def login(request):
#     return render(request, 'MainApp/login.html')

def groups(request):
	return render(request, 'MainApp/groups.html')
