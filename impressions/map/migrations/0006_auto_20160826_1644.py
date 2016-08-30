# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-26 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20160718_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layer',
            options={'verbose_name': 'Era'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['site_type', 'short_name']},
        ),
        migrations.AddField(
            model_name='layer',
            name='ordinal',
            field=models.IntegerField(default=99, verbose_name='Order of Eras'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='layer_index',
            field=models.IntegerField(default=0, verbose_name='Base layer index'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='sites',
            field=models.ManyToManyField(blank=True, to='map.Site'),
        ),
    ]
