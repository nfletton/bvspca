from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, PageManager
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from bvspca.core.models_abstract import Attachable, MenuTitleable


class NewsManager(PageManager):

    def news(self, limit=None):
        news = self.live().order_by('-first_published_at')
        if limit:
            return news[:limit]
        return news


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

    objects = NewsManager()

    parent_page_types = ['news.NewsPage']
    subpage_type = []

    search_fields = Page.search_fields + [
        index.SearchField('details'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('details'),
        ImageChooserPanel('main_photo'),
        StreamFieldPanel('attachments'),
    ]

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class NewsPage(Page, MenuTitleable):
    """
    News list view
    """
    subpage_types = ['news.News']

    content_panels = [
        FieldPanel('title'),
    ]

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
