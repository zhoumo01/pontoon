# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-08 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0139_bug-1501168-ftl-remove-comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='priority',
        ),
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='date_disabled',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='resource',
            name='date_obsoleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='obsolete',
            field=models.BooleanField(default=False),
        ),
    ]