from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailsearch import index

from .blocks import ContentStreamBlock


class MenuTitleable(models.Model):
    menu_title = models.CharField(verbose_name='menu title', max_length=100, blank=True)

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    class Meta:
        abstract = True


class Attachable(models.Model):
    attachments = StreamField([
        ('document', DocumentChooserBlock()),
    ], blank=True)

    class Meta:
        abstract = True


class ContentPage(Page, MenuTitleable, Attachable):
    body = StreamField(ContentStreamBlock(), verbose_name="Page body", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = []

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body'),
        StreamFieldPanel('attachments'),
    ]

    class Meta:
        verbose_name = 'General Content Page'
