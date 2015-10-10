from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'nothing': "nothing"}
    return render(request, 'hacker_matcher/index.html', context_dict)

def profle_setup(request):
    return render(request, 'hacker_matcher/profile_setup.html')

def matches(request):
    return render(request, 'hacker_matcher/matches.html')