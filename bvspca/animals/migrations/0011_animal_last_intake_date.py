# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0010_auto_20171121_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='last_intake_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
