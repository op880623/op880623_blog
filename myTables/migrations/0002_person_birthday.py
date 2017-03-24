# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myTables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='birth date'),
            preserve_default=False,
        ),
    ]
