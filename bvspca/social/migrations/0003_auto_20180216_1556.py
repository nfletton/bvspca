# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-16 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20180212_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaqueue',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp'),
        ),
    ]