# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-08 18:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20160826_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layer',
            options={'ordering': ['ordinal'], 'verbose_name': 'Era'},
        ),
    ]
