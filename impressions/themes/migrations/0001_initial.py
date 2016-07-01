# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-30 23:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_auto_20160630_1326'),
        ('supporting', '0008_auto_20160630_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('menu_blurb', models.TextField(blank=True, default='')),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Production Notes')),
                ('edited_by', models.CharField(blank=True, default='', max_length=64)),
                ('edit_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='edit date')),
                ('title', models.CharField(max_length=64)),
                ('image_name', models.CharField(blank=True, default='', max_length=32)),
                ('narrative', models.TextField(blank=True, default='')),
                ('content_type', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.ContentType')),
                ('contexts', models.ManyToManyField(blank=True, to='supporting.Context', verbose_name='Contexts related to this item')),
                ('evidence', models.ManyToManyField(blank=True, to='supporting.EvidenceItem', verbose_name='Evidence items related to this item')),
                ('people', models.ManyToManyField(blank=True, to='supporting.Person', verbose_name='People related to this item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
