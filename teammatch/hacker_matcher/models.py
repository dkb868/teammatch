from django.db import models

# Create your models here.
class Hacker(models.Model):
	name = models.CharField()
	languages_pro = models.ManyToManyField(Languages, blank = True)
	languages_noob = models.ManyToManyField(Languages, blank = True)
	team = models.ForeignKey(Team, blank = True)
	slack = models.CharField()
	is_competitive = models.BooleanField()
	education_school = models.CharField(max_length = 2, choices = school_options)
	education_year = models.CharField(max_length = 2, choices = year_in_school_options)
	project_genre_wanted = models.ForeignKey(Genres, blank = True)
	

school_options = (
	('HS', 'High School'),
	('CL', 'College'),
	('OT', 'Other')
)
year_in_school_options = (
	('FR', "Freshman"),
	("SO", "Sophomore"),
	("JR", "Junior"),
	("SR", 'Senior')
)
	
class Languages(models.Model):
	name = models.CharField()

	
class Team(models.Model):
	name = models.CharField()
	languages = models.ManyToManyField(Languages)
	project = models.ForeignKey(Project)
	team_owner = models.ForeignKey(Hacker)
	languages_wanted = models.ManyToManyField(Languages)
	
class Project(models.Model):
	name = models.CharField()
	genre = models.ForeignKey(Genres)
	platform = models.ManyToManyField(Platforms)

class Genres(models.Model):
	name = models.CharField()
	 
class Platforms(models.Model):
	name = models.CharField()
	platform_type = models.CharField()
