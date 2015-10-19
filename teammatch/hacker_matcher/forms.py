__author__ = 'mitri'

from django import forms
from hacker_matcher.models import Hacker, Team, JoinRequest


class HackerForm(forms.ModelForm):

    class Meta:
        model = Hacker
        exclude = ('teams',)

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ('team_owner',)

class JoinRequestForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        exclude = ('user','team')