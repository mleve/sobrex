# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170106_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='Client',
            new_name='client',
        ),
    ]
