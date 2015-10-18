from django.shortcuts import render
from django.http import HttpResponse
from hacker_matcher.forms import HackerForm
from hacker_matcher.models import Team, Hacker, Compatability




def index(request):
    context_dict = {'nothing': "nothing"}
    return render(request, 'hacker_matcher/index.html', context_dict)

def matches(request):
    # Testing the general idea of the algorithm
    # Get teams and hacker

    current_hacker = Hacker.objects.get(user=request.user)

    # Get all the compatabilities that the user already has
    compatability_already_done = Compatability.objects.filter(hacker = current_hacker)
    # get all teams whose compatability is in the above variable,
    # i.e who have a compatability with the current hacker already
    team_already_done = Team.objects.filter(compatability__in=compatability_already_done)
    print team_already_done
    # get list of teams that user doesn't already have compatability with
    teams = Team.objects.exclude(id__in=team_already_done)
    print teams
    # Compare hacker to every team and create a compatability object for this relation
    for x in teams:

        # ALGORITHM GOES HERE
        score = 3 # ALGORITHM RESULT GOES HERE
        # Create the new compatability with the score from the algortihm.
        # This only affects teams that it has not alraedy been calculated for
        compatability = Compatability.objects.create(hacker = current_hacker, team = x, value = score )
        compatability.save()

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

            return matches(request)
        else:
            print form.errors

    else:
        form = HackerForm()
    context_dict = {'form': form}
    return render(request, 'hacker_matcher/profile_setup.html', context_dict)
