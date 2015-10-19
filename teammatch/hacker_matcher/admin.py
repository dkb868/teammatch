from django.contrib import admin
from hacker_matcher.models import Hacker, Languages, Team, Genres, Platforms, Compatability, Experience, JoinRequest

admin.site.register(Hacker)
admin.site.register(Languages)
admin.site.register(Team)
admin.site.register(Genres)
admin.site.register(Platforms)
admin.site.register(Compatability)
admin.site.register(Experience)
admin.site.register(JoinRequest)