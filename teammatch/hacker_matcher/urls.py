__author__ = 'mitri'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^profile_setup/', views.profile_setup, name='profile_setup'),
        url (r'^matches/', views.matches, name='matches'),
        url (r'^signup/', views.signup, name='signup'),
        url (r'^create_team/', views.create_team, name='create_team'),
        url (r'^your_teams/', views.your_teams, name='your_teams'),
        url (r'^team_profile/(?P<team_id>\d+)/$', views.team_profile, name='team_profile'),
        url (r'^join_request/(?P<team_id>\d+)/$', views.join_request, name='join_request'), )

