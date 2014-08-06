# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shape_Points',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Latitude', models.FloatField(default=None)),
                ('Longitude', models.FloatField(default=None)),
                ('Shape_ID', models.CharField(max_length=10, default=-1)),
                ('route', models.ForeignKey(to='User.Route')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='route',
            name='Route_ID',
            field=models.CharField(max_length=20, default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stop',
            name='Latitude',
            field=models.FloatField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stop',
            name='Longitude',
            field=models.FloatField(default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stop',
            name='Stop_ID',
            field=models.CharField(max_length=15, default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 4, 14, 45, 34, 396336)),
        ),
        migrations.AlterField(
            model_name='position',
            name='Latitude',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='position',
            name='Longitude',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='DeviceID',
            field=models.IntegerField(default=-1),
        ),
    ]
