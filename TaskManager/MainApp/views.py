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
		if request.is_ajax():
			group_list = Group.objects.filter(users = request.user)
			return render_to_response('MainApp/groups.html', {'user':request.user, 'group_list':group_list})
		else:
			return HttpResponseRedirect("/")
	else:
		#messages.error(request, 'User not authorized.')
		return HttpResponseRedirect("/login")

def groups_new(request):
	if request.user.is_authenticated():
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
		#messages.error(request, 'User not authorized.')
		return HttpResponseRedirect("/login")

def groups_view(request, group_id):
    if request.user.is_authenticated():
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
    else:
        #messages.error(request, 'User not authorized.')
        return HttpResponseRedirect("/login")
        # NEED TO RETURN LIST OF RELATED TASKS TOO

