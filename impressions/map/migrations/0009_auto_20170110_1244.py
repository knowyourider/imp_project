# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-10 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20170102_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='overlay',
            options={'ordering': ['ordinal']},
        ),
        migrations.AlterField(
            model_name='layer',
            name='ordinal',
            field=models.IntegerField(default=99, verbose_name='List order'),
        ),
        migrations.AlterField(
            model_name='overlay',
            name='ordinal',
            field=models.IntegerField(default=99, verbose_name='List order'),
        ),
    ]
