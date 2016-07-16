# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-13 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporting', '0009_auto_20160709_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Caption'),
        ),
        migrations.AlterField(
            model_name='evidenceitem',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Caption'),
        ),
        migrations.AlterField(
            model_name='fastfact',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Caption'),
        ),
        migrations.AlterField(
            model_name='person',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Caption'),
        ),
        migrations.AlterField(
            model_name='place',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Caption'),
        ),
        migrations.AlterField(
            model_name='special',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Image Caption'),
        ),
    ]