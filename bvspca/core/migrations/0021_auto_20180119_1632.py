# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 23:32
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20180119_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactformpage',
            name='close',
        ),
        migrations.RemoveField(
            model_name='contactformpage',
            name='embedded_map',
        ),
        migrations.AlterField(
            model_name='contactformpage',
            name='intro',
            field=wagtail.core.fields.StreamField((('heading_block', wagtail.core.blocks.StructBlock((('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))))), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', label='Paragraph')), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))))), ('document_block', wagtail.core.blocks.StructBlock((('document', wagtail.documents.blocks.DocumentChooserBlock(required=True)),))), ('external_link', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock())))), ('block_quote', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))))), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-external-link-square', label='Embedded Media', template='core/blocks/embed_block.html')), ('table_block', wagtail.core.blocks.StructBlock((('table', wagtail.contrib.table_block.blocks.TableBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))))), ('raw_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()),))), ('donate_button', wagtail.core.blocks.StructBlock((('button_name', wagtail.core.blocks.CharBlock(default='Donate5.png')),)))), blank=True, verbose_name='Details'),
        ),
    ]
