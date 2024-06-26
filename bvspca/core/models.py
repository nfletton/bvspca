from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from bvspca.animals.models import Animal, AnimalCountSettings
from bvspca.core.blocks import HeadingBlock, SliderBlock, SupporterBlock, TeamMemberBlock
from bvspca.events.models import Event
from bvspca.news.models import News
from .blocks import ContentStreamBlock
from .forms import WagtailCaptchaFormBuilder, remove_captcha_field
from .models_abstract import Attachable, MenuTitleable, SendMailMixin, PageDesignMixin


class ContentPage(Page, MenuTitleable, Attachable, PageDesignMixin):
    body = StreamField(ContentStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    subpage_types = []

    content_panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        FieldPanel('attachments'),
    ] + PageDesignMixin.content_panels

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    def title_size(self):
        if len(self.title) > 50:
            return 'small'
        if len(self.title) > 30:
            return 'medium'
        return 'large'

    class Meta:
        verbose_name = 'General Content Page'


class HomePage(Page):
    slider = StreamField([
        ('slider_item', SliderBlock())
    ], blank=True, use_json_field=True)

    events_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This image MUST BE EXACTLY 1400px by 530px',
    )

    parent_page_types = ['wagtailcore.Page']

    search_fields = Page.search_fields + [
    ]

    content_panels = [
        FieldPanel('title'),
        FieldPanel('slider'),
        FieldPanel('events_photo')
    ]

    class Meta:
        verbose_name = 'Home Page'

    def get_context(self, request, *args, **kwargs):
        # Update template context
        context = super(HomePage, self).get_context(request, args, kwargs)
        context['events'] = Event.objects.future(4)
        context['news'] = News.objects.news(3)
        context['random_animals'] = Animal.objects.random(7)
        context['animal_counts'] = AnimalCountSettings.objects.get(pk=2)
        return context

    @property
    def has_multiple_slides(self):
        active_slides = 0;
        for slide in self.slider:
            if slide.value['active']:
                active_slides += 1
            if active_slides > 1:
                return True
        return False


class SupportersPage(Page, MenuTitleable, PageDesignMixin):
    supporters = StreamField([
        ('category', HeadingBlock()),
        ('supporter', SupporterBlock()),
    ], blank=True, use_json_field=True)
    body = StreamField(ContentStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True)

    parent_page_types = []
    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('supporters'),
    ]

    content_panels = [
        FieldPanel('title'),
        FieldPanel('supporters'),
        FieldPanel('body'),
    ] + PageDesignMixin.content_panels

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    class Meta:
        verbose_name = 'Supporters Page'


class TeamPage(Page, MenuTitleable, PageDesignMixin):
    group1_title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='title',
    )
    group1_members = StreamField([
        ('member', TeamMemberBlock())
    ], blank=True, verbose_name='members', use_json_field=True)
    group2_title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='title',
    )
    group2_members = StreamField([
        ('member', TeamMemberBlock())
    ], blank=True, verbose_name='members', use_json_field=True)
    group3_title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='title',
    )
    group3_members = StreamField([
        ('member', TeamMemberBlock())
    ], blank=True, verbose_name='members', use_json_field=True)

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('group1_members'),
        index.SearchField('group2_members'),
        index.SearchField('group3_members'),
    ]

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('group1_title'),
            FieldPanel('group1_members'),
        ],
            heading="Team Group 1",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel([
            FieldPanel('group2_title'),
            FieldPanel('group2_members'),
        ],
            heading="Team Group 2",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel([
            FieldPanel('group3_title'),
            FieldPanel('group3_members'),
        ],
            heading="Team Group 3",
            classname="collapsible collapsed"
        ),
    ] + PageDesignMixin.content_panels

    parent_page_types = []
    subpage_types = []

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
    dogs_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='dogs banner image',
        help_text='This image should be exactly 1400px wide and 370px high.'
    )
    dogs_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    cats_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='cats banner image',
        help_text='This image should be exactly 1400px wide and 370px high.'
    )
    cats_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    parent_page_types = []

    content_panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            [
                FieldPanel('dogs_image'),
                PageChooserPanel('dogs_page'),
            ],
            heading='Dogs page link',
        ),
        MultiFieldPanel(
            [
                FieldPanel('cats_image'),
                PageChooserPanel('cats_page'),
            ],
            heading='Cats page link',
        ),
    ]

    class Meta:
        verbose_name = 'Adoption Centre'


class WagtailCaptchaEmailForm(AbstractEmailForm):
    """Pages implementing a captcha form with email notification should inherit from this"""

    form_builder = WagtailCaptchaFormBuilder

    def process_form_submission(self, form):
        remove_captcha_field(form)
        return super().process_form_submission(form)

    class Meta:
        abstract = True


class ContactFormField(AbstractFormField):
    page = ParentalKey('ContactFormPage', related_name='form_fields')


class ContactFormPage(MenuTitleable, WagtailCaptchaEmailForm):
    column_1 = StreamField(ContentStreamBlock(), blank=True, use_json_field=True)
    column_2 = StreamField(ContentStreamBlock(), blank=True, use_json_field=True)
    thank_you_text = RichTextField(blank=True)

    parent_page_types = []
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('column_1'),
        FieldPanel('column_2'),
        FieldPanel('thank_you_text'),
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldPanel('to_address', classname="full"),
            FieldPanel('from_address', classname="full"),
            FieldPanel('subject', classname="full"),
        ], "Email")
    ]

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]


class ContentIndexPage(MenuTitleable, Page, PageDesignMixin):
    intro = RichTextField(blank=True)
    empty_message = models.CharField(max_length=200, default='Empty')

    subpage_types = [ContentPage]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('empty_message'),
    ] + PageDesignMixin.content_panels

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]


class RedirectPage(Page):
    """
    A page to provide a mechanism to add menu items that redirect to another page,
    a document or an external site.
    """
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    new_tab = models.BooleanField(
        'Open in new tab',
        blank=True,
        default=False,
    )

    subpage_types = []
    content_panels = [
        FieldPanel('title'),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        FieldPanel('link_document'),
        FieldPanel('new_tab')
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    def clean(self):
        link_field_names = ['link_external', 'link_page', 'link_document']
        set_fields_count = 0
        for field_name in link_field_names:
            if getattr(self, field_name, None):
                set_fields_count += 1
        # at least one link field should be set
        if not set_fields_count:
            error = ValidationError('one (and only one) of these link fields must be set', code='not_allowed')
            errors = {}
            for field_name in link_field_names:
                errors[field_name] = error
            raise ValidationError(errors)
        # only one link field can be set
        if set_fields_count > 1:
            error = ValidationError('only one of these link fields can be set', code='not_allowed')
            errors = {}
            for field_name in link_field_names:
                if getattr(self, field_name, None):
                    errors[field_name] = error
            raise ValidationError(errors)

    class Meta:
        verbose_name = 'Redirect Page'

    def serve(self, request):
        return redirect(self.link, permanent=False)
