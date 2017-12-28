from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django_ical.views import ICalFeed
from wagtail.wagtailcore.models import Page

from bvspca.events.models import Event
from bvspca.animals.models import Animal
from bvspca.news.models import News


class SpcaFeed(Feed):
    def item_pubdate(self, item):
        return item.first_published_at


class AllContentFeed(SpcaFeed):
    title = 'Bow Valley SPCA - All Content - All'
    link = 'https://www.bowvalleyspca.org/all/'
    description = 'Bow Valley SPCA Content'

    def items(self):
        return Page.objects.live().specific().filter(depth__gt=1).order_by('-first_published_at')[:50]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        if hasattr(item, 'description'):
            description = item.description
        else:
            if hasattr(item, 'details'):
                description = item.details
            else:
                description = item.title
        return truncatewords_html(description, 100)

    def item_link(self, item):
        return item.full_url


class AnimalsFeed(SpcaFeed):
    title = 'Bow Valley SPCA Animals'
    link = 'https://www.bowvalleyspca.org/animals/'
    description = 'Bow Valley SPCA Adoptable Animals'

    def items(self):
        return Animal.objects.live().order_by('-first_published_at')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(item.description, 100)

    def item_link(self, item):
        return item.full_url


class LatestNewsFeed(SpcaFeed):
    title = 'Bow Valley SPCA News'
    link = 'https://www.bowvalleyspca.org/news/'
    description = 'Bow Valley SPCA New'

    def items(self):
        return News.objects.live().order_by('-first_published_at')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(item.details, 100)

    def item_link(self, item):
        return item.full_url


class EventFeed(ICalFeed):
    product_id = '-//atesl.ca//Example//EN'
    timezone = 'MST'
    file_name = 'event.ics'

    def items(self):
        return Event.objects.live().order_by('-start_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(item.details, 100)

    def item_start_datetime(self, item):
        return item.start_date

    def item_end_datetime(self, item):
        return item.end_date

    def item_link(self, item):
        return item.full_url
