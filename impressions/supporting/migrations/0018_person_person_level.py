# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-09 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporting', '0017_auto_20161024_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_level',
            field=models.IntegerField(choices=[(3, 'Related'), (2, 'Important'), (1, 'Hitchcocks')], default=0),
        ),
    ]
