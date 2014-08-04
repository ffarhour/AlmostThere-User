# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20140804_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 4, 19, 34, 32, 363185)),
        ),
        migrations.AlterField(
            model_name='shape_point',
            name='Shape_ID',
            field=models.CharField(default=-1, max_length=10),
        ),
        migrations.AlterField(
            model_name='stop_time',
            name='time',
            field=models.TimeField(default=datetime.datetime(2014, 8, 4, 19, 34, 32, 367190)),
        ),
    ]
