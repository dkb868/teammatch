__author__ = 'mitri'

from django import forms
from hacker_matcher.models import Hacker

class HackerForm(forms.ModelForm):

    class Meta:
        model = Hacker
        fields = ('name',)