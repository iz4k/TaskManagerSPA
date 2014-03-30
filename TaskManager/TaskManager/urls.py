from django.conf.urls import patterns, include, url
from django.contrib import admin

from MainApp.views import home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TaskManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('login.urls')),
    url(r'', include('MainApp.urls')),
)