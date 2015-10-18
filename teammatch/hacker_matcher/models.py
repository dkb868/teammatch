from django.db import models
from django.contrib.auth.models import User

# User Profile
class Hacker(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    name = models.CharField(max_length = 150, blank = True, null=True)
    languages_pro = models.ManyToManyField('Languages', blank = True, related_name = 'hacker_languages_pro', null=True)
    languages_noob = models.ManyToManyField('Languages', blank = True, related_name = 'hacker_languages_noob', null=True)
    is_competitive = models.BooleanField(blank=True, default=True)
    genres = models.ManyToManyField('Genres', blank = True, null = True)
    platforms = models.ManyToManyField('Platforms', related_name = 'hacker_platforms_wanted',blank = True, null = True)
    experience = models.ForeignKey('Experience',blank=True,null=True)
    # Many to many field used to store compatability between hacker and teams
    teams = models.ManyToManyField('Team', through='Compatability', null=True)
    
    def __unicode__(self):
        return self.name

class Team(models.Model):
    team_owner = models.ForeignKey('Hacker',blank = True, null = True)
    name = models.CharField(max_length = 150,blank = True, null = True)
    languages = models.ManyToManyField('Languages', related_name = 'team_languages_wanted',blank = True, null = True)
    is_competitive = models.BooleanField(blank=True, default=True)
    genres = models.ManyToManyField('Genres', blank = True, null = True)
    platforms = models.ManyToManyField('Platforms', related_name = 'team_platforms_wanted',blank = True, null = True)
    experience = models.ManyToManyField('Experience',blank=True,null=True)

    def __unicode__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name

class Platforms(models.Model):
    name = models.CharField(max_length = 50)
    platform_type = models.CharField(max_length = 50, blank=True, null=True)
    def __unicode__(self):
        return self.name

# Gives the compatability between a hacker and a team
# Used as a through table between Hacker and Team
class Compatability(models.Model):
    value = models.FloatField(blank=True,null=True)
    hacker = models.ForeignKey('Hacker')
    team = models.ForeignKey('Team')

    def __unicode__(self):
        return unicode(self.value) + " Between " + unicode(self.hacker) + " and " + unicode(self.team)