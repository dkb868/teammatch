# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('slack', models.CharField(max_length=50)),
                ('is_competitive', models.BooleanField()),
                ('education_school', models.CharField(max_length=2, choices=[(b'HS', b'High School'), (b'CL', b'College'), (b'GS', b'Graduate Student'), (b'GR', b'Graduated')])),
                ('education_year', models.CharField(max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('school_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('platform_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('genre', models.ForeignKey(to='hacker_matcher.Genres')),
                ('platform', models.ManyToManyField(to='hacker_matcher.Platforms')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('languages', models.ManyToManyField(related_name='team_languages', to='hacker_matcher.Languages')),
                ('languages_wanted', models.ManyToManyField(related_name='team_languages_wanted', to='hacker_matcher.Languages')),
                ('project', models.ForeignKey(to='hacker_matcher.Project')),
                ('team_owner', models.ForeignKey(to='hacker_matcher.Hacker')),
            ],
        ),
        migrations.AddField(
            model_name='hacker',
            name='languages_noob',
            field=models.ManyToManyField(related_name='hacker_languages_noob', null=True, to='hacker_matcher.Languages', blank=True),
        ),
        migrations.AddField(
            model_name='hacker',
            name='languages_pro',
            field=models.ManyToManyField(related_name='hacker_languages_pro', null=True, to='hacker_matcher.Languages', blank=True),
        ),
        migrations.AddField(
            model_name='hacker',
            name='platforms_wanted',
            field=models.ForeignKey(related_name='hacker_platforms_wanted', to='hacker_matcher.Platforms'),
        ),
        migrations.AddField(
            model_name='hacker',
            name='project_genre_wanted',
            field=models.ForeignKey(blank=True, to='hacker_matcher.Genres', null=True),
        ),
        migrations.AddField(
            model_name='hacker',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
