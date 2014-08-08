# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_auto_20140808_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 8, 14, 52, 10, 315324)),
        ),
        migrations.AlterField(
            model_name='stop_time',
            name='time',
            field=models.TimeField(default=datetime.datetime(2014, 8, 8, 14, 52, 10, 323330)),
        ),
    ]
