# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20140804_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='Bus_ID',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 4, 15, 21, 21, 876375)),
        ),
        migrations.AlterField(
            model_name='route',
            name='Route_ID',
            field=models.CharField(max_length=20, default=-1, unique=True),
        ),
        migrations.AlterField(
            model_name='shape_points',
            name='Shape_ID',
            field=models.CharField(max_length=10, default=-1, unique=True),
        ),
        migrations.AlterField(
            model_name='stop',
            name='Stop_ID',
            field=models.CharField(max_length=15, default=-1, unique=True),
        ),
        migrations.AlterField(
            model_name='stop_times',
            name='time',
            field=models.TimeField(default=datetime.datetime(2014, 8, 4, 15, 21, 21, 879377)),
        ),
        migrations.AlterField(
            model_name='trip',
            name='TripID',
            field=models.CharField(max_length=25, default=-1, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='DeviceID',
            field=models.IntegerField(default=-1, unique=True),
        ),
    ]
