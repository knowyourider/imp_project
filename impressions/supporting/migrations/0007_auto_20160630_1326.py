# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-30 17:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160630_1326'),
        ('supporting', '0006_context_context_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('menu_blurb', models.TextField(blank=True, default='')),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Production Notes')),
                ('edited_by', models.CharField(blank=True, default='', max_length=64)),
                ('edit_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='edit date')),
                ('status_num', models.IntegerField(choices=[(0, '0 - Initial Entry'), (1, '1 - Place Holder'), (2, '2 - Real Shortname'), (3, '3 - Candidate for Publication'), (4, '4 - Published')], default=0)),
                ('title', models.CharField(max_length=128)),
                ('narrative', models.TextField(blank=True, default='', verbose_name='Description / Label')),
                ('caption', models.CharField(blank=True, default='', max_length=255)),
                ('content_type', models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='core.ContentType')),
            ],
            options={
                'verbose_name': 'Place of Interest',
            },
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('menu_blurb', models.TextField(blank=True, default='')),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Production Notes')),
                ('edited_by', models.CharField(blank=True, default='', max_length=64)),
                ('edit_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='edit date')),
                ('status_num', models.IntegerField(choices=[(0, '0 - Initial Entry'), (1, '1 - Place Holder'), (2, '2 - Real Shortname'), (3, '3 - Candidate for Publication'), (4, '4 - Published')], default=0)),
                ('special_type', models.CharField(choices=[('animation', 'Animation'), ('slideshow', 'Slide Show')], default='animation', max_length=32)),
                ('title', models.CharField(max_length=128)),
                ('narrative', models.TextField(blank=True, default='', verbose_name='Description / Label')),
                ('caption', models.CharField(blank=True, default='', max_length=255)),
                ('content_type', models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='core.ContentType')),
            ],
            options={
                'verbose_name': 'Specail Features',
            },
        ),
        migrations.AddField(
            model_name='context',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='evidenceitem',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='fastfact',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='fastfact',
            name='fastfact_type',
            field=models.CharField(choices=[('definition', 'Definition'), ('moreinfo', 'More Info')], default='moreinfo', max_length=32),
        ),
        migrations.AddField(
            model_name='person',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='context',
            name='status_num',
            field=models.IntegerField(choices=[(0, '0 - Initial Entry'), (1, '1 - Place Holder'), (2, '2 - Real Shortname'), (3, '3 - Candidate for Publication'), (4, '4 - Published')], default=0),
        ),
        migrations.AlterField(
            model_name='evidenceitem',
            name='status_num',
            field=models.IntegerField(choices=[(0, '0 - Initial Entry'), (1, '1 - Place Holder'), (2, '2 - Real Shortname'), (3, '3 - Candidate for Publication'), (4, '4 - Published')], default=0),
        ),
        migrations.AlterField(
            model_name='fastfact',
            name='status_num',
            field=models.IntegerField(choices=[(0, '0 - Initial Entry'), (1, '1 - Place Holder'), (2, '2 - Real Shortname'), (3, '3 - Candidate for Publication'), (4, '4 - Published')], default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='status_num',
            field=models.IntegerField(choices=[(0, '0 - Initial Entry'), (1, '1 - Place Holder'), (2, '2 - Real Shortname'), (3, '3 - Candidate for Publication'), (4, '4 - Published')], default=0),
        ),
    ]