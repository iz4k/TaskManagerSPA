from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	users = models.ManyToManyField(User)
	created = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('MainApp.views.groups_view', args=[str(self.id)])

	def type(self):
		return self._meta.verbose_name

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		ordering = ["-created"]

class Task(models.Model):
	name = models.CharField(max_length=50)
	users = models.ManyToManyField(User)
	description = models.CharField(max_length=300)
	deadline = models.DateField()
	group = models.ForeignKey(Group, blank=True, null= True)
	priority = models.PositiveSmallIntegerField(blank=True, null= True)
	workload = models.FloatField(blank=True, null= True)
	created = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('MainApp.views.tasks_view', args=[str(self.id)])

	def type(self):
		return self._meta.verbose_name

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		ordering = ["-created"]


class Comment(models.Model):
	user = models.ForeignKey(User)
	comment = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)
	task = models.ForeignKey(Task, blank=True, null= True)
	group = models.ForeignKey(Group, blank=True, null= True)

	def get_absolute_url(self):
		return reverse('MainApp.views.comment_view', args=[str(self.id)])

	def type(self):
		return self._meta.verbose_name

	def __unicode__(self):
		return "Comment by "+unicode(self.user)+" on "+unicode(self.created)

	class Meta:
		ordering = ["-created"]
