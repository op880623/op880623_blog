# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTables', '0006_auto_20170324_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='hp',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
