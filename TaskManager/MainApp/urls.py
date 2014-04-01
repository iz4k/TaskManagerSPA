from django.conf.urls import patterns, include, url
from MainApp import views
urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^groups/$', views.groups),
    url(r'^groups/(?P<group_id>[0-9])/$', views.groups_view),    
    url(r'^groups_new/', views.groups_new),
    url(r'^tasks/$', views.tasks),
    url(r'^tasks/(?P<task_id>[0-9])/$', views.tasks_view),   
    url(r'^tasks_new/', views.tasks_new),
    url(r'^profile/$', views.profile)
)
