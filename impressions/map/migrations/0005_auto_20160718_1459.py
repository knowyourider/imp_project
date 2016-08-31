# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-18 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_layer_layer_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='era_description',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='layer',
            name='slug',
            field=models.SlugField(max_length=32, unique=True, verbose_name='Layer short name'),
        ),
    ]