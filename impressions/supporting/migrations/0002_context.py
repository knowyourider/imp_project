# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-28 22:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160201_1346'),
        ('supporting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('menu_blurb', models.TextField(blank=True, default='')),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Production Notes')),
                ('edited_by', models.CharField(blank=True, default='', max_length=64)),
                ('edit_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='edit date')),
                ('status_num', models.IntegerField(choices=[(1, '1 - Entered'), (2, '2 - TBD'), (3, '3 - Work in progress'), (4, '4 - Published')], default=0)),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(blank=True, default='', max_length=128)),
                ('narrative', models.TextField(blank=True, default='', verbose_name='Description / Label')),
                ('content_type', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='core.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
