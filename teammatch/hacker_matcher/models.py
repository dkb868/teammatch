from django.db import models
from django.contrib.auth.models import User

# Create your models here.
school_options = (
    ('HS', 'High School'),
    ('CL', 'College'),
    ('GS', 'Graduate Student'),
    ('GR', 'Graduated'),
)
year_in_school_options = (
    ('FR', "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", 'Senior'),
)

class Hacker(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    name = models.CharField(max_length = 150, blank = True, null = True)
    languages_pro = models.ManyToManyField('Languages', blank = True, null = True, related_name = 'hacker_languages_pro')
    languages_noob = models.ManyToManyField('Languages', blank = True, null = True, related_name = 'hacker_languages_noob')
    slack = models.CharField(max_length = 50, blank = True, null = True)
    is_competitive = models.BooleanField(blank=True, default=True)
    education_school = models.CharField(max_length = 2, choices = school_options, blank = True, null = True)
    education_year = models.CharField(max_length = 2, choices = year_in_school_options, blank = True, null = True)
    school_name = models.CharField(max_length = 150, blank = True, null = True)
    project_genre_wanted = models.ForeignKey('Genres', blank = True, null = True)
    platforms_wanted = models.ForeignKey('Platforms', related_name = 'hacker_platforms_wanted', blank = True, null = True)
    
    def __unicode__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length = 150)
    languages = models.ManyToManyField('Languages', related_name = 'team_languages')
    project = models.ForeignKey('Project')
    team_owner = models.ForeignKey('Hacker')
    languages_wanted = models.ManyToManyField('Languages', related_name = 'team_languages_wanted')
    
    def __unicode__(self):
        return self.name 
           
class Project(models.Model):
    name = models.CharField(max_length = 150)
    genre = models.ForeignKey('Genres')
    platform = models.ManyToManyField('Platforms')
    
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