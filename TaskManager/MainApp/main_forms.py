from django import forms
from MainApp.models import *

class GroupForm(forms.ModelForm):
	class Meta:
	    model = Group
	    fields = ["name", "description", "users"]
	    widgets = {
	    	'description': forms.Textarea(),
	    	'users': forms.CheckboxSelectMultiple()
	    }

class GroupForm(forms.ModelForm):
	class Meta:
	    model = Task
	    fields = ["name","users" ,"description", "deadline", "group", "priority", "workload"]
	    widgets = {
	    	'description': forms.Textarea(),
	    	'users': forms.CheckboxSelectMultiple()
	    }