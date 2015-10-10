__author__ = 'mitri'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^profile_setup/$', views.profile_setup, name='profile_setup'),
        )

