# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-05 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTables', '0014_auto_20170327_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='eng_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='champion',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
