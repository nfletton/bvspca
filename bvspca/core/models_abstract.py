from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class MenuTitleable(models.Model):
    menu_title = models.CharField(verbose_name='menu title', max_length=100, blank=True)

    class Meta:
        abstract = True


class Attachable(models.Model):
    attachments = StreamField([
        ('document', DocumentChooserBlock()),
    ], blank=True)

    class Meta:
        abstract = True
