# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-09 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_source'),
        ('supporting', '0008_auto_20160630_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Source'),
        ),
        migrations.AddField(
            model_name='evidenceitem',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Source'),
        ),
        migrations.AddField(
            model_name='fastfact',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Source'),
        ),
        migrations.AddField(
            model_name='person',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Source'),
        ),
        migrations.AddField(
            model_name='place',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Source'),
        ),
        migrations.AddField(
            model_name='special',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Source'),
        ),
    ]