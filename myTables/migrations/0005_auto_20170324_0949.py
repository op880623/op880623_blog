# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 01:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myTables', '0004_auto_20170324_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 24, 1, 49, 26, 212367, tzinfo=utc), verbose_name='update date'),
        ),
    ]
