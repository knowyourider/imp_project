# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-02 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('special', '0008_auto_20170601_1527'),
        ('supporting', '0030_auto_20170601_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='featured_specials',
            field=models.ManyToManyField(blank=True, to='special.Feature', verbose_name='Special Features related to this item'),
        ),
        migrations.AddField(
            model_name='evidenceitem',
            name='featured_specials',
            field=models.ManyToManyField(blank=True, to='special.Feature', verbose_name='Special Features related to this item'),
        ),
    ]
