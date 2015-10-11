# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacker_matcher', '0002_auto_20151010_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platforms',
            name='platform_type',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
