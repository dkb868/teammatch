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
    for current_team in teams:
        score = 0.0
        # compare pro languages
        for language in current_hacker.languages_pro.all():
            if language in current_team.languages.all():
                # raw addition
                score += 3
                # weight
                # later maybe users can define weights for each section
                score *= 1.5

        # compare noob languages
        for language in current_hacker.languages_noob.all():
            if language in current_team.languages.all():
                score += 0.5
                score *= 1.1

        # compare genres
        for genre in current_hacker.genres.all():
            if genre in current_team.genres.all():
                score += 1
                score *= 1.1

        # compare platforms
        for platform in current_hacker.platforms.all():
            if platform in current_team.platforms.all():
                score += 1
                score *= 1.1

        # compare experience
        if (current_hacker.experience in current_team.experience.all()):
            score += 1
            score *= 1

        # If the competitive levels don't match, scale score down severely
        if (current_hacker.is_competitive != current_team.is_competitive):
            score *= 0.09

        # ALGORITHM GOES HERE
        # Create the new compatability with the score from the algortihm.
        # This only affects teams that it has not alraedy been calculated for
        compatability = Compatability.objects.create(hacker = current_hacker, team = current_team, value = score )
        compatability.save()

    # Finally, get the new list of compatability objects for current user
    # and add to context as match_list
    current_hacker_compatability_list = Compatability.objects.filter(hacker = current_hacker)
    context_dict = {'match_list': current_hacker_compatability_list}
    return render(request, 'hacker_matcher/matches.html', context_dict)

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
