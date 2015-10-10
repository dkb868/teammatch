from django.db import models

# Create your models here.
class Hacker(models.Model):
	name = models.CharField()
	languages_pro = models.ForeignKey(Languages)
	languages_noob = models.ForeignKey(Languages)
	teams = models.ManyToManyField(Team)
	slack = models.CharField()
	is_compettitive = models.BooleanField()
	education_school = models.CharField(max_length = 2, choices = school_options)
	education_year = models.CharField(max_length = 2, choices = year_in_school_options)


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
	project = models.OneToONeField(Project)
	
	
class Project(models.Model):
	name = models.CharField(max_length = )
	genre = models.ForeignKey(Genres)

class Genres(models.Model):
	name = models.CharField()
	 
