# Generated by Django 2.1.3 on 2019-03-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0026_animalspage_show_newsletter_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='animal',
            name='sub_location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
