# Generated by Django 2.0.4 on 2018-04-12 16:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20180403_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='group1_members',
            field=wagtail.core.fields.StreamField((('member', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=50)), ('role', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.core.blocks.RichTextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(help_text='Image should be at least 350px x 350px', required=False))))),), blank=True, verbose_name='members'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='group2_members',
            field=wagtail.core.fields.StreamField((('member', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=50)), ('role', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.core.blocks.RichTextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(help_text='Image should be at least 350px x 350px', required=False))))),), blank=True, verbose_name='members'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='group3_members',
            field=wagtail.core.fields.StreamField((('member', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=50)), ('role', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('role_since', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('location', wagtail.core.blocks.CharBlock(max_length=50, required=False)), ('pets', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('bio', wagtail.core.blocks.RichTextBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(help_text='Image should be at least 350px x 350px', required=False))))),), blank=True, verbose_name='members'),
        ),
    ]
