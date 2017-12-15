# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 21:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20171206_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='attachments',
            field=wagtail.wagtailcore.fields.StreamField((('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='fa-file-text')),), blank=True),
        ),
    ]