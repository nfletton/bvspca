# Generated by Django 2.0.3 on 2018-03-07 18:43

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20180306_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='slider',
            field=wagtail.fields.StreamField((('slider_item', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(max_length=25)), ('summary', wagtail.blocks.TextBlock(max_length=60)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.blocks.URLBlock(required=False))))),), blank=True),
        ),
    ]
