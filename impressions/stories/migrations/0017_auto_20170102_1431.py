# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-02 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_chapter_special_features'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['ordinal']},
        ),
    ]
