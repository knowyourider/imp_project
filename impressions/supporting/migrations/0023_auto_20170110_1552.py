# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-10 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporting', '0022_context_topics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['ordinal'], 'verbose_name': 'Backdrop Topic/Category'},
        ),
        migrations.AddField(
            model_name='evidenceitem',
            name='accession_num',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='evidenceitem',
            name='is_circa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='context',
            name='priority_num',
            field=models.IntegerField(choices=[(1, '1 - highest priority'), (2, '2 - important'), (3, '3 - nice to have'), (5, '5 - TBD'), (9, '9 - not using')], default=5),
        ),
    ]