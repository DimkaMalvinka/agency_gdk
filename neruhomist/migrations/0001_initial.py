# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.IntegerField()),
                ('room_count', models.IntegerField()),
                ('floor_count', models.IntegerField()),
                ('ploshcha', models.IntegerField()),
                ('rieltor_tel', models.IntegerField()),
                ('about', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('house', models.ForeignKey(to='neruhomist.House', related_name='images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SellType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='house',
            name='house_type',
            field=models.ForeignKey(to='neruhomist.HouseType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='house',
            name='sell_type',
            field=models.ForeignKey(to='neruhomist.SellType'),
            preserve_default=True,
        ),
    ]
