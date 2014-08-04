# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20140804_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop_Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=datetime.datetime(2014, 8, 4, 15, 40, 9, 309566))),
                ('stop', models.ForeignKey(to='User.Stop')),
                ('trip', models.ForeignKey(to='User.Trip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='stop_times',
            name='stop',
        ),
        migrations.RemoveField(
            model_name='stop_times',
            name='trip',
        ),
        migrations.DeleteModel(
            name='Stop_Times',
        ),
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 4, 15, 40, 9, 307565)),
        ),
    ]
