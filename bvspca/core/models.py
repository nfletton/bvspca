from django.conf import settings
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from bvspca.events.models import Event
from bvspca.news.models import NewsPage
from .blocks import ContentStreamBlock
from .models_abstract import Attachable, MenuTitleable


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


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']

    search_fields = Page.search_fields + [
    ]

    content_panels = [
        FieldPanel('title'),
    ]

    class Meta:
        verbose_name = 'Home Page'

    def get_context(self, request, *args, **kwargs):
        # Update template context
        context = super(HomePage, self).get_context(request, args, kwargs)
        context['events'] = Event.objects.future(settings.SPCA_LIST_BLOCK_LENGTH)
        # context['news'] = NewsPage.news(settings.SPCA_LIST_BLOCK_LENGTH)
        return context
