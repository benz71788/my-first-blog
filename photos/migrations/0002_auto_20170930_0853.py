# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='created_at',
        ),
        migrations.AddField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='photo',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
