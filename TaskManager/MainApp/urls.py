from django.conf.urls import patterns, include, url
from MainApp import views
urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^groups/$', views.groups),
    url(r'^groups/(?P<group_id>[0-9]*)/$', views.groups_view),
    url(r'^groups_new/', views.groups_new),
    url(r'^tasks/$', views.tasks),
    url(r'^tasks/(?P<task_id>[0-9]*)/$', views.tasks_view),
    url(r'^tasks_new/', views.tasks_new),
    url(r'^profile/$', views.profile),
    url(r'^profile/(?P<user_id>[0-9]*)/$', views.user_view),
    url(r'^comment/(?P<comment_id>[0-9]*)/$', views.comment_view),
    url(r'^small_task_list/$', views.small_task_list),
    url(r'^calendarjson/$', views.calendarjson),
    url(r'^calendarmore/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.calendarmore)

)
