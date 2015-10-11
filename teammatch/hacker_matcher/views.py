from django.shortcuts import render
from django.http import HttpResponse
from hacker_matcher.forms import HackerForm
import hacker_matcher.models
from matchalgorithm import matches, Hacker, Profile




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
    list_of_profs = []
    for x in list_of_other_persons:
        list_of_profs.append(Profile(x.name, [ y.name for y in x.languages_pro.all()], [y.name for y in x.languages_noob.all()], x.project_genre_wanted, x.platforms_wanted.name, x.is_competitive, x.id))
    list_of_matches = matches(hax, list_of_profs)
    #list of matches is reverse sorted, and the second item.id is the id of the person you're matched with.
    
    for x in list_of_matches:
        matches = hacker_matcher.models.Hacker.objects.get(id = x[1].id)
    #matches is the list ofHacker objects considered the closest matches.
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
