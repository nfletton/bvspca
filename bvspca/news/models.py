from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, PageManager
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from bvspca.core.blocks import ContentStreamBlock
from bvspca.core.models_abstract import Attachable, MenuTitleable, PageDesignMixin


class NewsManager(PageManager):

    def news(self, limit=None):
        news = self.live().order_by('-first_published_at')
        if limit:
            return news[:limit]
        return news

    def previous(self, current_news_item_date):
        previous = self.live()\
            .filter(first_published_at__lt=current_news_item_date)\
            .order_by('-first_published_at').first()
        return previous if previous else None

    def next(self, current_news_item_date):
        next = self.live()\
            .filter(first_published_at__gt=current_news_item_date)\
            .order_by('-first_published_at').last()
        return next if next else None


class News(Page, Attachable):
    """
    An individual news item
    """
    details = RichTextField(verbose_name='details')
    main_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    extra_details = StreamField(ContentStreamBlock(required=False), verbose_name="Extra Content", blank=True)

    objects = NewsManager()

    parent_page_types = ['news.NewsPage']
    subpage_type = []

    search_fields = Page.search_fields + [
        index.SearchField('details'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_photo'),
        FieldPanel('details'),
        StreamFieldPanel('extra_details'),
        StreamFieldPanel('attachments'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('first_published_at')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(News, self).get_context(request, args, kwargs)
        context['previous'] = News.objects.previous(current_news_item_date=self.first_published_at)
        context['next'] = News.objects.next(current_news_item_date=self.first_published_at)
        return context

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class NewsPage(Page, MenuTitleable, PageDesignMixin):
    """
    News list view
    """
    subpage_types = ['news.News']

    content_panels = [
        FieldPanel('title'),
    ] + PageDesignMixin.content_panels

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    def get_context(self, request, *args, **kwargs):
        news = News.objects.news()

        page = request.GET.get('page', 1)
        paginator = Paginator(news, settings.SPCA_LIST_PAGE_LENGTH)

        try:
            news = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            news = paginator.page(1)

        context = super(NewsPage, self).get_context(request, args, kwargs)
        context['news'] = news
        return context
