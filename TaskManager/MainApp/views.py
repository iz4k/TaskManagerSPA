from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from MainApp.models import *
from main_forms import *

def home(request):

    if request.user.is_authenticated():
        user = request.user
        return render_to_response('MainApp/home.html', {'user':request.user})
    else:
        #messages.error(request, 'User not authorized.')
        return HttpResponseRedirect("/login")


def groups(request):

	if request.user.is_authenticated():
		
		group_list = Group.objects.filter(users = request.user)
		return render_to_response('MainApp/groups.html', {'user':request.user, 'group_list':group_list})
	else:
		#messages.error(request, 'User not authorized.')
		return HttpResponseRedirect("/login")

def groups_new(request):
	# if request.method == 'POST': # If the form has been submitted...
	# 	# ContactForm was defined in the the previous section
	# 	form = GroupForm(request.POST) # A form bound to the POST data
	# 	if form.is_valid(): # All validation rules pass
	# 		# Process the data in form.cleaned_data
	# 		# ...
	# 		return HttpResponseRedirect('/') # Redirect after POST
	# else:
	form = GroupForm() # An unbound form

	#return render_to_response('MainApp/groups_new.html', context_instance=RequestContext(request, {'form': form}))
	return render_to_response('MainApp/groups_new.html',{'user':request.user, 'form':form}) 