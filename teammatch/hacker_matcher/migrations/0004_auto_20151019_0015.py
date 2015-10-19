# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hacker_matcher', '0003_auto_20151011_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compatability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='project',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='hacker',
            name='education_school',
        ),
        migrations.RemoveField(
            model_name='hacker',
            name='education_year',
        ),
        migrations.RemoveField(
            model_name='hacker',
            name='platforms_wanted',
        ),
        migrations.RemoveField(
            model_name='hacker',
            name='project_genre_wanted',
        ),
        migrations.RemoveField(
            model_name='hacker',
            name='school_name',
        ),
        migrations.RemoveField(
            model_name='hacker',
            name='slack',
        ),
        migrations.RemoveField(
            model_name='team',
            name='languages_wanted',
        ),
        migrations.RemoveField(
            model_name='team',
            name='project',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_owner',
        ),
        migrations.AddField(
            model_name='hacker',
            name='genres',
            field=models.ManyToManyField(to='hacker_matcher.Genres', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='hacker',
            name='platforms',
            field=models.ManyToManyField(related_name='hacker_platforms_wanted', null=True, to='hacker_matcher.Platforms', blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='genres',
            field=models.ManyToManyField(to='hacker_matcher.Genres', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='is_competitive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='platforms',
            field=models.ManyToManyField(related_name='team_platforms_wanted', null=True, to='hacker_matcher.Platforms', blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='languages',
            field=models.ManyToManyField(related_name='team_languages_wanted', null=True, to='hacker_matcher.Languages', blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='joinrequest',
            name='team',
            field=models.ForeignKey(blank=True, to='hacker_matcher.Team', null=True),
        ),
        migrations.AddField(
            model_name='joinrequest',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='compatability',
            name='hacker',
            field=models.ForeignKey(to='hacker_matcher.Hacker'),
        ),
        migrations.AddField(
            model_name='compatability',
            name='team',
            field=models.ForeignKey(to='hacker_matcher.Team'),
        ),
        migrations.AddField(
            model_name='hacker',
            name='experience',
            field=models.ForeignKey(blank=True, to='hacker_matcher.Experience', null=True),
        ),
        migrations.AddField(
            model_name='hacker',
            name='teams',
            field=models.ManyToManyField(to='hacker_matcher.Team', null=True, through='hacker_matcher.Compatability'),
        ),
        migrations.AddField(
            model_name='team',
            name='experience',
            field=models.ManyToManyField(to='hacker_matcher.Experience', null=True, blank=True),
        ),
    ]
