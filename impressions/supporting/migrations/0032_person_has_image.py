# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporting', '0031_auto_20170602_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='has_image',
            field=models.BooleanField(default=True),
        ),
    ]