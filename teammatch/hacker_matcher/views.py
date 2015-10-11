from django.shortcuts import render
from django.http import HttpResponse
from hacker_matcher.forms import HackerForm
import hacker_matcher.models
from machalgorithm import matches, Hacker, prof




def index(request):
    context_dict = {'nothing': "nothing"}
    return render(request, 'hacker_matcher/index.html', context_dict)

def profle_setup(request):
    return render(request, 'hacker_matcher/profile_setup.html')

def matches(request):
    hacker = hacker_matcher.models.Hacker.objects.get(user = request.user)
    team = hacker_matcher.models.Team.objects.get(team_owner = hacker)
    languages_needed = [x.name for x in team.languages_wanted.all()]
    genre_needed = team.project.genre.name
    platforms_needed = [ x.name for x in team.project.platform.all()]
    mentor_id = hacker.id
    list_of_other_persons = hacker_matcher.models.Hacker.objects.exclude(id = hacker.id)
    hax = Hacker(languages_needed, genre_needed, platforms_needed, hacker.is_competitive)
    list_of_profs
    for x in list_of_other_persons:
        [prof(x.name, x.languages_pro, x.languages_noob, ) for y ]
    
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

            return index(request)
        else:
            print form.errors

    else:
        form = HackerForm()
    context_dict = {'form': form}
    return render(request, 'hacker_matcher/profile_setup.html', context_dict)
