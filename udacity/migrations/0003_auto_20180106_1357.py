# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-06 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udacity', '0002_art_coords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='coords',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
