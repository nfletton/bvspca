# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 16:53
from __future__ import unicode_literals

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20171207_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teampage',
            name='members',
        ),
        migrations.AddField(
            model_name='teampage',
            name='group1_members',
            field=wagtail.fields.StreamField((('category', wagtail.blocks.StructBlock((('name', wagtail.blocks.CharBlock(max_length=50)), ('role', wagtail.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.blocks.CharBlock(max_length=100, required=False)), ('bio', wagtail.blocks.TextBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('photo_caption', wagtail.blocks.CharBlock(max_length=50, required=False))))),), blank=True),
        ),
    ]
