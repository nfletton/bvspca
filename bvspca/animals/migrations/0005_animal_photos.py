# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 17:19
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_animalspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='photos',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock()),), blank=True),
        ),
    ]
