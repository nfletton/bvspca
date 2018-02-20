import datetime

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils.html import strip_tags
from django.utils.text import Truncator
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, PageManager
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from bvspca.core.blocks import ContentStreamBlock
from bvspca.core.models_abstract import Attachable, MenuTitleable, MetaTagable


class EventManager(PageManager):

    def future(self, limit=None):
        events = self.live().filter(
            Q(start_date__gte=datetime.date.today()) | Q(end_date__gte=datetime.date.today()),
        ).order_by('start_date')
        if limit:
            return events[:limit]
        return events


class Event(Page, MetaTagable, Attachable):
    details = RichTextField(verbose_name='details')
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date', blank=True, null=True)
    main_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contact_name = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=15, blank=True)
    website = models.URLField(max_length=200, blank=True)

    extra_details = StreamField(ContentStreamBlock(required=False), verbose_name="Extra Content", blank=True)

    objects = EventManager()

    search_fields = Page.search_fields + [
        index.SearchField('details'),
    ]

    subpage_types = []
    content_panels = Page.content_panels + [
        ImageChooserPanel('main_photo'),
        FieldRowPanel([
            FieldPanel('start_date'),
            FieldPanel('end_date'),
        ]),
        FieldPanel('details'),
        FieldPanel('contact_name'),
        FieldPanel('contact_email'),
        FieldPanel('contact_phone'),
        FieldPanel('website'),
        StreamFieldPanel('extra_details'),
        StreamFieldPanel('attachments'),
    ]

    def save(self, *args, **kwargs):
        if not self.end_date or self.start_date > self.end_date:
            self.end_date = self.start_date
        super(Event, self).save(*args, **kwargs)

    def formatted_date(self):
        #  todo: move to a template tag??
        if self.start_date == self.end_date:
            return self.start_date.strftime('%a, %d %b %Y')
        return self.start_date.strftime('%a, %d %b ') + '&ndash;' + self.end_date.strftime(' %a, %d %b %Y')

    def seo_and_social_meta_values(self):
        data = super().seo_and_social_meta_values()
        if self.main_photo:
            data['photo'] = self.main_photo
            data['social_title'] = self.title
            data['social_description'] = Truncator(strip_tags(self.details)).chars(200).replace("[\r|\n].", "")
            data['site_name'] = settings.WAGTAIL_SITE_NAME
            data['page_url'] = self.full_url
        return data

    def __str__(self):
        return self.title


class EventsPage(Page, MenuTitleable):
    content_panels = [
        FieldPanel('title'),
    ]

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    def get_context(self, request, *args, **kwargs):
        context = super(EventsPage, self).get_context(request, args, kwargs)
        context['events'] = Event.objects.future()
        return context

    def __str__(self):
        return self.title


Event.parent_page_types = [EventsPage]
EventsPage.subpage_types = [Event]
