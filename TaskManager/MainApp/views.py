from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from MainApp.models import *
from main_forms import *
import sys
def home(request):

	print >>sys.stderr, 'TEST PRINT PLS IGNORE'
	user = request.user
	return render_to_response('MainApp/home.html', {'user':request.user})

def groups(request):

	
	if request.is_ajax():
		group_list = Group.objects.filter(users = request.user)
		return render_to_response('MainApp/groups.html', {'user':request.user, 'group_list':group_list})
	else:
		return HttpResponseRedirect("/")


def groups_new(request):
	if request.is_ajax():
		if request.method == 'POST': # If the form has been submitted...
			form = GroupForm(request.POST) # A form bound to the POST data
			if form.is_valid(): # All validation rules pass
				form.save()
				return HttpResponseRedirect("/groups") # Redirect after POST
		else:
			form = GroupForm() # An unbound form

		#return render_to_response('MainApp/groups_new.html', context_instance=RequestContext(request, {'form': form}))
		return render_to_response('MainApp/groups_new.html',{'user':request.user, 'form':form}, context_instance=RequestContext(request)) 
	else:
		return HttpResponseRedirect("/")


def groups_view(request, group_id):
    
	if request.is_ajax():
		user = request.user
		try:
			group = Group.objects.get(id = group_id)
		except Group.DoesNotExist:
			#some sort of error page here?
			return HttpResponseRedirect("/")
		#need to check if user is in group here
		return render_to_response('MainApp/group.html', {'group':group})
	else:
		return HttpResponseRedirect("/")


def tasks(request):
	if request.is_ajax():		
		return render_to_response('MainApp/tasks.html', {'user':request.user})
	else:
		return HttpResponseRedirect("/")
	
def profile(request):
	if request.is_ajax():
		group_list = Group.objects.filter(users = request.user)
		return render_to_response('MainApp/profile.html', {'user':request.user})
	else:
		return HttpResponseRedirect("/")
