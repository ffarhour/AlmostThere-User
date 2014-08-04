# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20140804_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop_Times',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('time', models.TimeField(default=datetime.datetime(2014, 8, 4, 15, 14, 31, 684901))),
                ('stop', models.ForeignKey(to='User.Stop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('TripID', models.CharField(default=-1, max_length=25)),
                ('direction', models.IntegerField(default=-1)),
                ('route', models.ForeignKey(to='User.Route')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stop_times',
            name='trip',
            field=models.ForeignKey(to='User.Trip'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 4, 15, 14, 31, 682899)),
        ),
    ]
