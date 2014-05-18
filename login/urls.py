from django.conf.urls import patterns, include, url,static

from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', views.login),
    url(r'^new_user/$',views.new_user),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

)
