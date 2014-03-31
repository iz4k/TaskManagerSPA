from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def home(request):

    if request.user.is_authenticated():
        user = request.user
        return render_to_response('MainApp/home.html', {'user':request.user})
    else:
        #messages.error(request, 'User not authorized.')
        return HttpResponseRedirect("/login")


def groups(request):

	if request.user.is_authenticated():
		user = request.user
		return render_to_response('MainApp/groups.html', {'user':request.user})
	else:
		#messages.error(request, 'User not authorized.')
		return HttpResponseRedirect("/login")
