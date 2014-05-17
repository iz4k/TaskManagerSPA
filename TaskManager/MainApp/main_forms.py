from django import forms
from MainApp.models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
import datetime

class GroupForm(forms.ModelForm):
	class Meta:
	    model = Group
	    fields = ["name", "description", "users"]
	    widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control'}),
	    	'description': forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
	    	'users': forms.CheckboxSelectMultiple()
	    }

class TaskForm(forms.ModelForm):
	
	class Meta:
	    model = Task
	    fields = ["name","users" ,"description", "deadline", "group", "priority", "workload"]
	    widgets = {
	    	'name' : forms.TextInput(attrs={'class':'form-control'}),
	    	'description': forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
	    	'users': forms.CheckboxSelectMultiple(),
	    	'priority': forms.Select(choices=(('1', 'High'),('2', 'Medium'),('3', 'Low'),)),
	    	'deadline': forms.DateInput()
	    }

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["comment"]
		widgets = {
			'comment': forms.Textarea()
		}