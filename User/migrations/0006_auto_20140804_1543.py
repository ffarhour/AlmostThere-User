# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20140804_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 4, 15, 43, 54, 915398)),
        ),
        migrations.AlterField(
            model_name='stop_time',
            name='time',
            field=models.TimeField(default=datetime.datetime(2014, 8, 4, 15, 43, 54, 918400)),
        ),
    ]
