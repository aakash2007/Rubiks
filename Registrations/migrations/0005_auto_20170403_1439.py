# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrations', '0004_auto_20170403_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='dept',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='psrn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
