# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-10 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporting', '0020_auto_20170102_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=24, unique=True, verbose_name='Topic short name')),
                ('title', models.CharField(max_length=64)),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order')),
            ],
            options={
                'ordering': ['ordinal'],
            },
        ),
        migrations.AlterModelOptions(
            name='context',
            options={'ordering': ['ordinal'], 'verbose_name': 'Backdrop'},
        ),
        migrations.AddField(
            model_name='context',
            name='priority_num',
            field=models.IntegerField(choices=[(1, '1 - highest priority'), (2, '2 - important'), (3, '3 - nice to have'), (5, '8 - TBD'), (9, '9 - not using')], default=5),
        ),
    ]
