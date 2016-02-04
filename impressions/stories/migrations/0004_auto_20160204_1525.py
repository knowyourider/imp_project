# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160204_1514'),
        ('evidence', '0005_auto_20160204_1514'),
        ('stories', '0003_auto_20160204_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='evidence_item',
            field=models.ManyToManyField(blank=True, to='evidence.EvidenceItem', verbose_name='evidence items related to this chapter'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='narrative',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='chapter',
            name='people',
            field=models.ManyToManyField(blank=True, to='people.Person', verbose_name='People related to this chapter'),
        ),
    ]
