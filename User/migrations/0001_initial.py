# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Bus_ID', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('DateTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bus_Position',
            fields=[
                ('position_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='User.Position', serialize=False)),
                ('bus', models.ForeignKey(to='User.Bus')),
            ],
            options={
            },
            bases=('User.position',),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('DeviceID', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Position',
            fields=[
                ('position_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='User.Position', serialize=False)),
                ('user', models.ForeignKey(to='User.User')),
            ],
            options={
            },
            bases=('User.position',),
        ),
    ]
