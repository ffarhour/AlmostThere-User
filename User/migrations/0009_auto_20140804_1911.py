# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20140804_1902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shape_Points',
            new_name='Shape_Point',
        ),
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 4, 19, 11, 30, 847457)),
        ),
        migrations.AlterField(
            model_name='stop_time',
            name='time',
            field=models.TimeField(default=datetime.datetime(2014, 8, 4, 19, 11, 30, 850391)),
        ),
    ]
