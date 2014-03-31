from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'MainApp.views.home'),
    url(r'^groups/$', 'MainApp.views.groups'),
    url(r'^groups_new/', 'MainApp.views.groups_new'),
)
