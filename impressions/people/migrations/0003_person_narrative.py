# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160204_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='narrative',
            field=models.TextField(blank=True, default=''),
        ),
    ]
