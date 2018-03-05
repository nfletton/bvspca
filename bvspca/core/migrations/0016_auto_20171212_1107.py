# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 18:07
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20171212_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='group1_members',
            field=wagtail.core.fields.StreamField((('member', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=50)), ('role', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))))),), blank=True, verbose_name='members'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='group2_members',
            field=wagtail.core.fields.StreamField((('member', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=50)), ('role', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))))),), blank=True, verbose_name='members'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='group3_members',
            field=wagtail.core.fields.StreamField((('member', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=50)), ('role', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.core.blocks.TextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))))),), blank=True, verbose_name='members'),
        ),
    ]
