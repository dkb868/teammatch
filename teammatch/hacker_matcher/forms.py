__author__ = 'mitri'

from django import forms
from hacker_matcher.models import Hacker

dhoices = (
    ('1', 'Java'),
    ('2', 'Python'),
    ('3', 'Ruby'),
    ('4', 'Swift'),
)

class HackerForm(forms.ModelForm):

    languages_pro = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=dhoices)
    class Meta:
        model = Hacker
        exclude = ('',)