# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('attachments', wagtail.fields.StreamField((('document', wagtail.documents.blocks.DocumentChooserBlock()),), blank=True)),
                ('details', wagtail.fields.RichTextField(verbose_name='details')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('contact_name', models.CharField(blank=True, max_length=100)),
                ('contact_email', models.EmailField(blank=True, max_length=100)),
                ('contact_phone', models.CharField(blank=True, max_length=15)),
                ('website', models.URLField(blank=True)),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='EventsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('menu_title', models.CharField(blank=True, max_length=100, verbose_name='menu title')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
