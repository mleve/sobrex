# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161229_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispatchorder',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='dispatchorder',
            name='sender',
        ),
        migrations.AddField(
            model_name='dispatchorder',
            name='destination_address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='app.Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispatchorder',
            name='pick_up_address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pick_up', to='app.Address'),
            preserve_default=False,
        ),
    ]