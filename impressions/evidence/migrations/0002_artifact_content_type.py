# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160201_1346'),
        ('evidence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='content_type',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='core.ContentType'),
        ),
    ]