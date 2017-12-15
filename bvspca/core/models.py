from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from bvspca.core.blocks import HeadingBlock, PictureLinkBlock, SupporterBlock, TeamMemberBlock
from bvspca.events.models import Event
from bvspca.news.models import News
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

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

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
        context['news'] = News.objects.news(settings.SPCA_LIST_BLOCK_LENGTH)
        return context


class SupportersPage(Page, MenuTitleable):
    supporters = StreamField([
        ('category', HeadingBlock()),
        ('supporter', SupporterBlock()),
    ], blank=True)
    subpage_types = []

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('supporters'),
    ]

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    class Meta:
        verbose_name = 'Supporters Page'


class TeamPage(Page, MenuTitleable):
    group1_title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='title',
    )
    group1_members = StreamField([
        ('member', TeamMemberBlock())
    ], blank=True, verbose_name='members')
    group2_title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='title',
    )
    group2_members = StreamField([
        ('member', TeamMemberBlock())
    ], blank=True, verbose_name='members')
    group3_title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='title',
    )
    group3_members = StreamField([
        ('member', TeamMemberBlock())
    ], blank=True, verbose_name='members')

    subpage_types = []

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('group1_title'),
            StreamFieldPanel('group1_members'),
        ],
            heading="Team Group 1",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel([
            FieldPanel('group2_title'),
            StreamFieldPanel('group2_members'),
        ],
            heading="Team Group 2",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel([
            FieldPanel('group3_title'),
            StreamFieldPanel('group3_members'),
        ],
            heading="Team Group 3",
            classname="collapsible collapsed"
        ),
    ]

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    def team_groups(self):
        return [
            (self.group1_title, self.group1_members),
            (self.group2_title, self.group2_members),
            (self.group3_title, self.group3_members),
        ]

    class Meta:
        verbose_name = 'Team Page'


class ParentPage(Page):
    """
    A page for parent pages with no content. If a request is targeted at the page,
    the request is redirected to the first subpage if one exists. Otherwise the request
    is redirected to the home page
    """
    content_panels = [
        FieldPanel('title'),
    ]

    class Meta:
        verbose_name = 'Parent Page with No Content'

    def serve(self, request, *args, **kwargs):
        first_subpage = self.get_children().live().first()
        if first_subpage:
            return HttpResponseRedirect(first_subpage.url)
        return HttpResponseRedirect('/')


class AdoptionCentre(Page, MenuTitleable):
    """
    Top level navigation page where all things related to animal adoption
    are located as submenus items e.g. available dogs and cats,
    adoption policy, fees, etc.
    """
    body = StreamField([
        ('picture_links', ListBlock(PictureLinkBlock(), template='core/blocks/picture_links.html'))
    ], blank=True)

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Adoption Centre'
