# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-19 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0017_auto_20170102_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='is_vertical',
            field=models.BooleanField(default=False),
        ),
    ]
