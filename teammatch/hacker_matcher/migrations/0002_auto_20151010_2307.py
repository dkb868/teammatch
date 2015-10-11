# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_matcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hacker',
            name='education_school',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'HS', b'High School'), (b'CL', b'College'), (b'GS', b'Graduate Student'), (b'GR', b'Graduated')]),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='education_year',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')]),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='is_competitive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='name',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='platforms_wanted',
            field=models.ForeignKey(related_name='hacker_platforms_wanted', blank=True, to='hacker_matcher.Platforms', null=True),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='school_name',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='slack',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
