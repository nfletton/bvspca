# Generated by Django 2.0.4 on 2018-10-29 17:21

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20181024_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='slider',
            field=wagtail.fields.StreamField((('slider_item', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(max_length=25, required=False)), ('summary', wagtail.blocks.TextBlock(max_length=60, required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(help_text='This image MUST BE EXACTLY 1400px by 550px')), ('page', wagtail.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(required=False)), ('active', wagtail.blocks.BooleanBlock(required=False))))),), blank=True),
        ),
    ]
