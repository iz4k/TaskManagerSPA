from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	users = models.ManyToManyField(User)

	def __unicode__(self):
		return unicode(self.name)

class Task(models.Model):
	name = models.CharField(max_length=50)
	users = models.ManyToManyField(User)
	description = models.CharField(max_length=300)
	deadline = models.DateField()
	group = models.ForeignKey(Group)
	priority = models.PositiveSmallIntegerField()
	workload = models.FloatField()

	def __unicode__(self):
		return unicode(self.name)

class Comment(models.Model):
	user = models.ForeignKey(User)
	comment = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)
	task = models.ForeignKey(Task)
	group = models.ForeignKey(Group)

	def __unicode__(self):
		return unicode(self.user + "'s comment")