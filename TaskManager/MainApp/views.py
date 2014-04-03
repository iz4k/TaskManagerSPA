from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from MainApp.models import *
from main_forms import *
import sys

from django.template.loader import render_to_string



def ajax_view(function):
	#decorator function
	def _view(request, *args, **kwargs):

		response = function(request, *args, **kwargs)
		if request.is_ajax():
			return HttpResponse(response);
		else: 
			return render_to_response('MainApp/main.html',{'user':request.user, 'content':response})


	return _view	



@login_required
@ajax_view
def home(request):
	print >>sys.stderr, 'TEST PRINT PLS IGNORE'
	user = request.user
	return render_to_string('MainApp/home.html', {'user':request.user})


@login_required
@ajax_view
def groups(request):	
	group_list = Group.objects.filter(users = request.user)
	return render_to_string('MainApp/groups.html', {'user':request.user, 'group_list':group_list})
	
		
@login_required
@ajax_view
def groups_new(request):
	
	if request.method == 'POST': # If the form has been submitted...
		form = GroupForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			return groups(request)# Redirect after POST
	else:
		form = GroupForm() # An unbound form
	
	#return render_to_response('MainApp/groups_new.html', context_instance=RequestContext(request, {'form': form}))
	return render_to_string('MainApp/groups_new.html',{'user':request.user, 'form':form}, context_instance=RequestContext(request)) 



@login_required	
@ajax_view
def groups_view(request, group_id):

	user = request.user
	try:
		group = Group.objects.get(id = group_id)
	except Group.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")
	#need to check if user is in group here
	return render_to_string('MainApp/group.html', {'group':group})

	if request.method == 'POST': # If the form has been submitted...
		form = CommentForm(request.POST) # A form bound to the POST data
	task_list = Task.objects.filter(group = group)
	comment_list = Comment.objects.filter(group = group)
	return render_to_string('MainApp/group.html', {'group':group, 'task_list':task_list, 'comment_list':comment_list, 'form':form}, context_instance=RequestContext(request))

@login_required
@ajax_view
def tasks(request):
	task_list = Task.objects.filter(users= request.user)
	return render_to_string('MainApp/tasks.html', {'user':request.user, 'task_list':task_list})

@login_required
@ajax_view
def tasks_new(request):
	
	if request.method == 'POST': # If the form has been submitted...
		form = TaskForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			return HttpResponseRedirect("/tasks") # Redirect after POST
	else:
		form = TaskForm() # An unbound form


	#return render_to_response('MainApp/groups_new.html', context_instance=RequestContext(request, {'form': form}))

	return render_to_string('MainApp/tasks_new.html',{'user':request.user, 'form':form}, context_instance=RequestContext(request)) 

@login_required
@ajax_view
def tasks_view(request, task_id):

	user = request.user
	try:
		task = Task.objects.get(id = task_id)
	except Task.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")

	if request.method == 'POST': # If the form has been submitted...
		form = CommentForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			new_comment = form.save(commit = False)
			new_comment.user = request.user
			new_comment.task = task
			new_comment.group = None
			new_comment.save()
			return HttpResponseRedirect("/") # Redirect after POST
	else:
		form = CommentForm() # An unbound form
	
	comment_list = Comment.objects.filter(task = task)
	return render_to_string('MainApp/task.html', {'task':task, 'comment_list':comment_list, 'form':form}, context_instance=RequestContext(request))


@login_required
@ajax_view
def comment_view(request, comment_id):

	try:
		comment = Comment.objects.get(id = comment_id)
	except Comment.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")
	#need to check if user is in group here
	return render_to_string('MainApp/comment.html', {'comment':comment})

@login_required
@ajax_view	
def profile(request):
	group_list = Group.objects.filter(users = request.user)
	return render_to_string('MainApp/profile.html', {'user':request.user})

@login_required
@ajax_view
def user_view(request, user_id):
	try:
		user = User.objects.get(id = user_id)
	except User.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")
	#need to check if user is in group here
	
	group_list = Group.objects.filter(users = user)
	return render_to_string('MainApp/user.html', {'user':user, 'group_list': group_list})
