# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-25 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('special', '0002_auto_20170218_1745'),
        ('stories', '0018_chapter_is_vertical'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='featured_specials',
            field=models.ManyToManyField(blank=True, to='special.Feature', verbose_name='New TRANSITIONAL Special Features related to this item'),
        ),
    ]
