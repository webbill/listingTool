from django.conf.urls import patterns, include, url


from listingtool.tool.views import *

urlpatterns = patterns('',
    url(r'^$', tool_index),
    url(r'^item/add/$', AddItem),
)
