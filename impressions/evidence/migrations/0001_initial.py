# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 19:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40, unique=True, verbose_name='short name')),
                ('menu_blurb', models.CharField(blank=True, default='', max_length=255)),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Production Notes')),
                ('edited_by', models.CharField(blank=True, default='', max_length=64)),
                ('edit_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='edit date')),
                ('status_num', models.IntegerField(choices=[(1, '1 - Entered'), (2, '2 - TBD'), (3, '3 - Work in progress'), (4, '4 - Published')], default=0)),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(blank=True, default='', max_length=128)),
                ('description', models.TextField(blank=True, default='', verbose_name='Short Description')),
                ('creator', models.CharField(blank=True, default='', max_length=64, verbose_name='maker/author')),
                ('initial_zoom', models.IntegerField(blank=True, null=True, verbose_name='Initial zoom - Default (blank) is 50 (%)')),
                ('initial_x', models.IntegerField(blank=True, null=True, verbose_name='X - Default (blank) is 0 (centered)')),
                ('materials', models.CharField(blank=True, default='', max_length=128)),
                ('measurements', models.CharField(blank=True, default='', max_length=128)),
                ('initial_y', models.IntegerField(blank=True, null=True, verbose_name='Y - Default (blank) is 0 (centered)')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
