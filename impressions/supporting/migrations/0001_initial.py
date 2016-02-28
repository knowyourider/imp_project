# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 21:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20160201_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('menu_blurb', models.TextField(blank=True, default='')),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Production Notes')),
                ('edited_by', models.CharField(blank=True, default='', max_length=64)),
                ('edit_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='edit date')),
                ('status_num', models.IntegerField(choices=[(1, '1 - Entered'), (2, '2 - TBD'), (3, '3 - Work in progress'), (4, '4 - Published')], default=0)),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(blank=True, default='', max_length=128)),
                ('narrative', models.TextField(blank=True, default='', verbose_name='Description / Label')),
                ('creator', models.CharField(blank=True, default='', max_length=64, verbose_name='maker/author')),
                ('creation_year', models.IntegerField(blank=True, null=True)),
                ('dimensions', models.CharField(blank=True, default='', max_length=128)),
                ('materials', models.CharField(blank=True, default='', max_length=128)),
                ('content_type', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='core.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EvidenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_document_oriented', models.BooleanField(verbose_name='Document-oriented: can have pages and/or transcripts')),
                ('title', models.CharField(max_length=32)),
                ('slug', models.SlugField(max_length=16, unique=True)),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
            ],
            options={
                'ordering': ['ordinal'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=48, unique=True, verbose_name='short name')),
                ('menu_blurb', models.TextField(blank=True, default='')),
                ('ordinal', models.IntegerField(default=99, verbose_name='Order in Menu')),
                ('notes', models.TextField(blank=True, default='', verbose_name='Production Notes')),
                ('edited_by', models.CharField(blank=True, default='', max_length=64)),
                ('edit_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='edit date')),
                ('status_num', models.IntegerField(choices=[(1, '1 - Entered'), (2, '2 - TBD'), (3, '3 - Work in progress'), (4, '4 - Published')], default=0)),
                ('first_name', models.CharField(blank=True, default='', max_length=32)),
                ('last_name', models.CharField(blank=True, default='', max_length=32)),
                ('title_prefix', models.CharField(blank=True, default='', max_length=16)),
                ('suffix', models.CharField(blank=True, default='', max_length=16)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
                ('death_year', models.IntegerField(blank=True, null=True)),
                ('narrative', models.TextField(blank=True, default='')),
                ('content_type', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='core.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='evidenceitem',
            name='evidence_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporting.EvidenceType'),
        ),
    ]