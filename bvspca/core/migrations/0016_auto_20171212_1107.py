# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 18:07
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20171212_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='group1_members',
            field=wagtail.wagtailcore.fields.StreamField((('member', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(max_length=50)), ('role', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.wagtailcore.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))),), blank=True, verbose_name='members'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='group2_members',
            field=wagtail.wagtailcore.fields.StreamField((('member', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(max_length=50)), ('role', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.wagtailcore.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))),), blank=True, verbose_name='members'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='group3_members',
            field=wagtail.wagtailcore.fields.StreamField((('member', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(max_length=50)), ('role', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.wagtailcore.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))))),), blank=True, verbose_name='members'),
        ),
    ]
