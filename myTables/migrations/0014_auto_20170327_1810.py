# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myTables', '0013_auto_20170327_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='champion',
            old_name='attackspeedoffset',
            new_name='attackspeed',
        ),
    ]
