from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from listingtool.tool.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'listingtool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tool/', include("listingtool.tool.urls")),
    url(r'^$', tool_index),
)
