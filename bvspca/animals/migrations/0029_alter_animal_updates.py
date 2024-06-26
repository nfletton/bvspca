# Generated by Django 3.2.13 on 2022-08-19 13:00

import bvspca.core.blocks
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0028_locationsponsor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='updates',
            field=wagtail.fields.StreamField([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', label='Paragraph')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('document_block', wagtail.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))])), ('external_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock())])), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('attribute_name', wagtail.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-external-link-square', label='Embedded Media', template='core/blocks/embed_block.html')), ('table_block', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock()), ('caption', wagtail.blocks.CharBlock(required=False))])), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock())])), ('donate_button', wagtail.blocks.StructBlock([('button_name', wagtail.blocks.CharBlock(default='Donate5.png'))])), ('accordion', bvspca.core.blocks.AccordionBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'link', 'document-link', 'ol', 'ul', 'blockquote', 'hr', 'superscript', 'subscript', 'image']))])))], blank=True, verbose_name='Animal Updates'),
        ),
    ]
