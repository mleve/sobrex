# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Client'),
        ),
    ]