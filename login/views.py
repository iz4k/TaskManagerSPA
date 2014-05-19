from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404,render
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.core.context_processors import csrf


# from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
from login_forms import *
    
def login(request):
    # If we submitted the form...
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/")#goes to the main page
        else:
            # Show an error page
            form = AuthenticationForm(request.POST)
            return render(request,'login.html',{'form':form}) 

    # If we didn't post, send the test cookie along with the login form.
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form}) 

def new_user(request):
    return HttpResponseRedirect('/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/") 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()#returns user
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            new_user = auth.authenticate(username=username, password=password)
            auth.login(request, new_user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    
    #print response
    return render(request, "register.html", {
        'form': form,
    })
  