from django import forms
from MainApp.models import *

class GroupForm(forms.ModelForm):
	class Meta:
	    model = Group
	    fields = ["name", "description", "users"]
	    widgets = {
	    	'users': forms.CheckboxSelectMultiple()
	    }