from django.contrib import admin
from MainApp.models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	display = ('name')
admin.site.register(Group)
admin.site.register(Task)
admin.site.register(Comment)
