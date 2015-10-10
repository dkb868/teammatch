from django.db import models

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
    name = models.CharField(max_length = 150)
    languages_pro = models.ManyToManyField('Languages', blank = True, related_name = 'hacker_languages_pro')
    languages_noob = models.ManyToManyField('Languages', blank = True, related_name = 'hacker_languages_noob')
    team = models.ForeignKey('Team', blank = True)
    slack = models.CharField(max_length = 50)
    is_competitive = models.BooleanField()
    education_school = models.CharField(max_length = 2, choices = school_options)
    education_year = models.CharField(max_length = 2, choices = year_in_school_options)
    school_name = models.CharField(max_length = 150)
    project_genre_wanted = models.ForeignKey('Genres', blank = True)
    platforms_wanted = models.ForeignKey('Platforms', related_name = 'hacker_platforms_wanted')

class Languages(models.Model):
    name = models.CharField(max_length = 50)


class Team(models.Model):
    name = models.CharField(max_length = 150)
    languages = models.ManyToManyField('Languages', related_name = 'team_languages')
    project = models.ForeignKey('Project')
    team_owner = models.ForeignKey('Hacker', related_name = 'team_owner')
    languages_wanted = models.ManyToManyField('Languages', related_name = 'team_languages_wanted')

class Project(models.Model):
    name = models.CharField(max_length = 150)
    genre = models.ForeignKey('Genres')
    platform = models.ManyToManyField('Platforms')

class Genres(models.Model):
    name = models.CharField(max_length = 50)

class Platforms(models.Model):
    name = models.CharField(max_length = 50)
    platform_type = models.CharField(max_length = 50)
