from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

from MainApp.models import *
from main_forms import *
import sys




@login_required
def home(request):
	print >>sys.stderr, 'TEST PRINT PLS IGNORE'
	user = request.user
	return render_to_response('MainApp/home.html', {'user':request.user})
    

def ajax_view(function):
	def _view(request, *args, **kwargs):
		if request.is_ajax():
			return function(request, *args, **kwargs)
		else: 
			#this could be better
			return HttpResponseRedirect("/")

	return _view	




@ajax_view
def groups(request):

	
	group_list = Group.objects.filter(users = request.user)
	return render_to_response('MainApp/groups.html', {'user':request.user, 'group_list':group_list})
	
		

@ajax_view
def groups_new(request):
	
	if request.method == 'POST': # If the form has been submitted...
		form = GroupForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			return HttpResponseRedirect("/groups") # Redirect after POST
	else:
		form = GroupForm() # An unbound form

	#return render_to_response('MainApp/groups_new.html', context_instance=RequestContext(request, {'form': form}))
	return render_to_response('MainApp/groups_new.html',{'user':request.user, 'form':form}, context_instance=RequestContext(request)) 

	
@ajax_view
def groups_view(request, group_id):

	user = request.user
	try:
		group = Group.objects.get(id = group_id)
	except Group.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")
	#need to check if user is in group here
	return render_to_response('MainApp/group.html', {'group':group})

@ajax_view
def tasks(request):
	
	return render_to_response('MainApp/tasks.html', {'user':request.user})

@ajax_view	
def profile(request):
	group_list = Group.objects.filter(users = request.user)
	return render_to_response('MainApp/profile.html', {'user':request.user})
	