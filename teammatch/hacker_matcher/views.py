from django.shortcuts import render
from django.http import HttpResponse
from hacker_matcher.forms import HackerForm
import hacker_matcher.models



def index(request):
    context_dict = {'nothing': "nothing"}
    return render(request, 'hacker_matcher/index.html', context_dict)

def matches(request):
    return render(request, 'hacker_matcher/matches.html')

def signup(request):
      return render(request, 'hacker_matcher/signup.html')

# stores profile information
def profile_setup(request):

    if request.method == 'POST':
        form = HackerForm(request.POST)

        if form.is_valid():
            hacker = form.save(commit=False)
            hacker.user = request.user
            hacker.save()
            form.save_m2m()

            return index(request)
        else:
            print form.errors

    else:
        form = HackerForm()
    context_dict = {'form': form}
    return render(request, 'hacker_matcher/profile_setup.html', context_dict)
