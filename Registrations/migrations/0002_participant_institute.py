# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='institute',
            field=models.CharField(default='', max_length=10),
        ),
    ]
