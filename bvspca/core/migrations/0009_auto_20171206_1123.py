# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('core', '0008_auto_20171128_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('menu_title', models.CharField(blank=True, max_length=100, verbose_name='menu title')),
                ('supporters', wagtail.core.fields.StreamField((('category', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('supporter', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=100)), ('summary', wagtail.core.blocks.TextBlock()), ('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)))))), blank=True)),
            ],
            options={
                'verbose_name': 'Supporters Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Paragraph')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('document_block', wagtail.core.blocks.StructBlock((('document', wagtail.documents.blocks.DocumentChooserBlock(required=True)),))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-external-link-square', label='Embedded Media', template='core/blocks/embed_block.html')), ('table_block', wagtail.core.blocks.StructBlock((('table', wagtail.contrib.table_block.blocks.TableBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()),)))), blank=True, verbose_name='Page body'),
        ),
    ]
