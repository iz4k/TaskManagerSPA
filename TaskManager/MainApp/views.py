from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest 
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

from MainApp.models import *
from main_forms import *
import sys
import json
import time

@login_required
def home(request):
	print >>sys.stderr, 'TEST PRINT PLS IGNORE'
	user = request.user
	return render_to_response('MainApp/home.html', {'user':request.user})

def ajax_view(function):
	#decorator function
	def _view(request, *args, **kwargs):
		if request.is_ajax() or request.method == 'POST':
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
		if form.errors:
			errorjson = send_errors(form.errors)
			return HttpResponseBadRequest(errorjson)
		if form.is_valid(): # All validation rules pass
			form.save()
	else:
		form = GroupForm() # An unbound form

	#return render_to_response('MainApp/groups_new.html', context_instance=RequestContext(request, {'form': form}))
	return render_to_response('MainApp/groups_new.html',{'user':request.user, 'form':form}, context_instance=RequestContext(request)) 

	
@ajax_view
def groups_view(request, group_id):
	#need to check if user is in group here
	try:
		group = Group.objects.get(id = group_id)
	except Group.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")

	if request.method == 'POST': # If the form has been submitted...
		form = CommentForm(request.POST) # A form bound to the POST data
		if form.errors:
			errorjson = send_errors(form.errors)
			return HttpResponseBadRequest(errorjson)
		if form.is_valid(): # All validation rules pass
			new_comment = form.save(commit = False)
			new_comment.user = request.user
			new_comment.task = None
			new_comment.group = group
			new_comment.save()
			return HttpResponseRedirect("/") # Redirect after POST
	else:
		form = CommentForm() # An unbound form

	task_list = Task.objects.filter(group = group)
	comment_list = Comment.objects.filter(group = group)
	return render_to_response('MainApp/group.html', {'group':group, 'task_list':task_list, 'comment_list':comment_list, 'form':form}, context_instance=RequestContext(request))

@ajax_view
def tasks(request):
	task_list = Task.objects.filter(users = request.user)
	return render_to_response('MainApp/tasks.html', {'user':request.user, 'task_list':task_list})

@ajax_view
def tasks_new(request):
	if request.method == 'POST': # If the form has been submitted...
		form = TaskForm(request.POST) # A form bound to the POST data
		if form.errors:
			errorjson = send_errors(form.errors)
			return HttpResponseBadRequest(errorjson)
		if form.is_valid(): # All validation rules pass
			form.save()
	else:
		form = TaskForm() # An unbound form

	#return render_to_response('MainApp/groups_new.html', context_instance=RequestContext(request, {'form': form}))
	return render_to_response('MainApp/tasks_new.html',{'user':request.user, 'form':form}, context_instance=RequestContext(request)) 

@ajax_view
def tasks_view(request, task_id):
	#need to check if user is in task here
	try:
		task = Task.objects.get(id = task_id)
	except Task.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")

	if request.method == 'POST': # If the form has been submitted...
		form = CommentForm(request.POST) # A form bound to the POST data
		if form.errors:
			errorjson = send_errors(form.errors)
			return HttpResponseBadRequest(errorjson)
		if form.is_valid(): # All validation rules pass
			new_comment = form.save(commit = False)
			new_comment.user = request.user
			new_comment.task = task
			new_comment.group = None
			new_comment.save()
	else:
		form = CommentForm() # An unbound form
	
	comment_list = Comment.objects.filter(task = task)
	return render_to_response('MainApp/task.html', {'task':task, 'comment_list':comment_list, 'form':form}, context_instance=RequestContext(request))


@ajax_view
def comment_view(request, comment_id):
	try:
		comment = Comment.objects.get(id = comment_id)
	except Comment.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")
	#need to check if user is in group here
	return render_to_response('MainApp/comment.html', {'comment':comment})

@ajax_view	
def profile(request):
	group_list = Group.objects.filter(users = request.user)
	return render_to_response('MainApp/profile.html', {'user':request.user})

@ajax_view
def user_view(request, user_id):
	try:
		user = User.objects.get(id = user_id)
	except User.DoesNotExist:
		#some sort of error page here?
		return HttpResponseRedirect("/")
	#need to check if user is in group here
	
	group_list = Group.objects.filter(users = user)
	return render_to_response('MainApp/user.html', {'user':user, 'group_list': group_list})
	
def send_errors(errors):
	errors_dict = {}
	for error in errors:
		e = errors[error]
		errors_dict[error] = unicode(e)
	return json.dumps(errors_dict)

def calendarjson(request):
    callback = request.GET.get('callback', '')
    start = request.GET.get('start', '')
    end = request.GET.get('end', '')

    try:
        task = Task.objects.filter(users=request.user)
    except Task.DoesNotExist:
	return HttpResponseRedirect("/")

    newArray = []
    for i in task:
        tmpDict = {}
        tmpDict['title'] = i.name
        tmpDict['start'] = time.mktime(i.deadline.timetuple())
        tmpDict['url'] = "http://localhost:8888/event/" + i.name
        newArray.append(tmpDict)

    newDict = {}
    newDict = newArray

    resp = json.dumps(newDict)
    if 'callback' in request.REQUEST:
        resp = callback + '(' + resp + ')'

    return HttpResponse(resp, content_type='application/json')



