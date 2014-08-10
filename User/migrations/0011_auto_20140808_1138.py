# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20140804_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='short_name',
            field=models.CharField(max_length=10, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 8, 11, 38, 39, 164977)),
        ),
        migrations.AlterField(
            model_name='stop_time',
            name='time',
            field=models.TimeField(default=datetime.datetime(2014, 8, 8, 11, 38, 39, 171982)),
        ),
    ]
