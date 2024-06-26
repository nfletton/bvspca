from django.conf import settings
from django.db import models
from django.db.models import ForeignKey
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page, PageManager
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from bvspca.core.blocks import ContentStreamBlock
from bvspca.core.models_abstract import MenuTitleable, MetaTagable, PageDesignMixin
from bvspca.social.models import SocialMediaPostable


class AnimalManager(PageManager):
    def random(self, count):
        return self.live().filter(adoption_date__isnull=True).order_by('?')[:count]

    def previous(self, pk, species):
        previous = self.live()\
            .filter(species=species, adoption_date__isnull=True, pk__gt=pk)\
            .order_by('-pk').last()
        return previous if previous else None

    def next(self, pk, species):
        next = self.live()\
            .filter(species=species, adoption_date__isnull=True, pk__lt=pk)\
            .order_by('-pk').first()
        return next if next else None


class Animal(Page, MetaTagable, SocialMediaPostable):
    # PetPoint read-only fields
    petpoint_id = models.PositiveIntegerField(
        verbose_name='petpoint animal id',
        unique=True,
    )
    stage = models.CharField(max_length=100, blank=True)
    species = models.CharField(max_length=200, blank=True)
    sex = models.CharField(max_length=10)
    primary_breed = models.CharField(max_length=100, blank=True)
    secondary_breed = models.CharField(max_length=100, blank=True)
    primary_color = models.CharField(max_length=100, blank=True)
    secondary_color = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='age in months')
    size = models.CharField(max_length=3)
    description = models.TextField(blank=True, max_length=8000)
    photo_1_url = models.URLField(blank=True)
    photo_2_url = models.URLField(blank=True)
    photo_3_url = models.URLField(blank=True)
    on_hold = models.BooleanField(default=False)
    special_needs = models.CharField(max_length=150, blank=True)
    no_dogs = models.BooleanField(default=False)
    no_cats = models.BooleanField(default=False)
    no_kids = models.BooleanField(default=False)
    lived_with_kids = models.CharField(max_length=10, default='Unknown')
    lived_with_animals = models.CharField(max_length=10, default='Unknown')
    lived_with_animal_types = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=30, blank=True)
    surrender_date = models.DateField(null=True, blank=True)
    last_intake_date = models.DateField(null=True, blank=True)
    adoption_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    sub_location = models.CharField(max_length=200, blank=True)
    # local updatable fields
    main_photo = ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+',
    )
    additional_photos = StreamField(
        [
            ('image', ImageChooserBlock())
        ],
        blank=True,
        use_json_field=True
    )
    adoption_message = models.TextField(blank=True)
    updates = StreamField(
        ContentStreamBlock(required=False),
        verbose_name='Animal Updates',
        blank=True,
        use_json_field=True
    )

    objects = AnimalManager()

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('primary_breed'),
        index.SearchField('secondary_breed'),
        index.SearchField('primary_color'),
        index.SearchField('secondary_color'),
        index.SearchField('size'),
        index.SearchField('description'),
        index.SearchField('adoption_message'),
    ]

    parent_page_types = ['animals.AnimalsPage']
    subpage_types = []

    content_panels = [
        FieldPanel('main_photo'),
        FieldPanel('additional_photos'),
        FieldPanel('adoption_message'),
        FieldPanel('updates'),
    ]

    def social_media_post_status(self):
        warnings = []

        if not self.main_photo:
            warnings.append("No main photo")
        if self.adoption_date and not self.adoption_message:
            warnings.append("Adopted but no adoption message")
        elif not self.description:
            warnings.append("No description")
        return warnings

    def social_media_post_text(self):
        if self.adoption_date:
            return self.adoption_message
        else:
            return self.description

    def social_media_post_image(self):
        return self.main_photo

    def plural_species(self):
        return '{}s'.format(self.species)

    @classmethod
    def create(cls, petpoint_data):
        return cls(**cls.map_fields(petpoint_data))

    @classmethod
    def map_fields(cls, petpoint_data):
        """
        Map local field names to PetPoint data values.
        :param petpoint_data: PetPointAnimal object
        :return: Dictionary of Animal model field names to PetPoint value
        """
        return {
            'petpoint_id': petpoint_data.ID,
            'stage': petpoint_data.Stage,
            'title': petpoint_data.AnimalName,
            'species': petpoint_data.Species,
            'sex': petpoint_data.Sex,
            'primary_breed': petpoint_data.PrimaryBreed,
            'secondary_breed': petpoint_data.SecondaryBreed,
            'primary_color': petpoint_data.PrimaryColor,
            'secondary_color': petpoint_data.SecondaryColor,
            'age': petpoint_data.Age,
            'size': petpoint_data.Size,
            'description': petpoint_data.Dsc,
            'photo_1_url': petpoint_data.Photo1,
            'photo_2_url': petpoint_data.Photo2,
            'photo_3_url': petpoint_data.Photo3,
            'on_hold': petpoint_data.OnHold,
            'special_needs': petpoint_data.SpecialNeeds,
            'no_dogs': petpoint_data.NoDogs,
            'no_cats': petpoint_data.NoCats,
            'no_kids': petpoint_data.NoKids,
            'lived_with_kids': petpoint_data.LivedWithChildren,
            'lived_with_animals': petpoint_data.LivedWithAnimals,
            'lived_with_animal_types': petpoint_data.LivedWithAnimalTypes,
            'weight': petpoint_data.BodyWeight,
            'surrender_date': petpoint_data.DateOfSurrender,
            'last_intake_date': petpoint_data.LastIntakeDate,
            'location': petpoint_data.Location,
            'sub_location': petpoint_data.Sublocation,
        }

    def updateAdoptableAnimal(self, petpoint_data):
        dirty = False
        field_map = self.map_fields(petpoint_data)
        for field_name, value in field_map.items():
            if getattr(self, field_name) != value:
                setattr(self, field_name, value)
                dirty = True
        if not self.live:
            # adoptable animals should be live
            self.live = True
            dirty = True
        if self.adoption_date or self.adoption_message:
            # adoptable animals should not have adoption data
            self.adoption_date = None
            self.adoption_message = ''
            dirty = True
        if dirty:
            self.save()
            return True
        return False

    def seo_and_social_meta_values(self):
        data = super().seo_and_social_meta_values()
        if self.main_photo:
            data['photo'] = self.main_photo
            if self.adoption_date:
                data['social_title'] = '{} has been adopted!'.format(self.title)
                data['social_description'] = \
                    'We are pleased to announce that {} found their forever home on {:%b %-d, %Y}.'.format(self.title, self.adoption_date)
            else:
                data['social_title'] = 'Say hello to {}'.format(self.title)
                data['social_description'] = \
                    '{} is looking for a forever home. Contact us for more information'.format(self.title)
            data['site_name'] = getattr(settings, 'WAGTAIL_SITE_NAME')
            data['page_url'] = self.full_url
        return data

    def get_context(self, request, *args, **kwargs):
        # Update template context
        context = super(Animal, self).get_context(request, args, kwargs)
        context['previous'] = Animal.objects.previous(pk=self.pk, species=self.species)
        context['next'] = Animal.objects.next(pk=self.pk, species=self.species)
        return context

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['adoption_date']),
            models.Index(fields=['last_intake_date']),
            models.Index(fields=['species', 'adoption_date', 'last_intake_date', ]),
        ]


class AnimalsPage(Page, MenuTitleable, PageDesignMixin):
    PETPOINT_CAT_CODE = 'Cat'
    PETPOINT_DOG_CODE = 'Dog'
    ANIMAL_TYPES = ((PETPOINT_CAT_CODE, PETPOINT_CAT_CODE), (PETPOINT_DOG_CODE, PETPOINT_DOG_CODE))
    species = models.CharField(max_length=20, choices=ANIMAL_TYPES)
    content_panels = [
        FieldPanel('title'),
        FieldPanel('species'),
    ] + PageDesignMixin.content_panels

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    parent_page_types = []
    subpage_types = ['animals.Animal']

    def animals(self):
        return Animal.objects.live()\
            .descendant_of(self)\
            .filter(adoption_date__isnull=True)\
            .order_by('-pk')

    def __str__(self):
        return self.title


@register_setting(icon='fa-paw')
class AnimalCountSettings(BaseSiteSetting):
    cats_adopted = models.PositiveIntegerField(default=0)
    cats_rescued = models.PositiveIntegerField(default=0)
    dogs_adopted = models.PositiveIntegerField(default=0)
    dogs_rescued = models.PositiveIntegerField(default=0)

    panels = [
        FieldPanel('cats_adopted'),
        FieldPanel('cats_rescued'),
        FieldPanel('dogs_adopted'),
        FieldPanel('dogs_rescued'),
    ]

    class Meta:
        verbose_name = 'animals counts'


@register_snippet
class LocationSponsor(models.Model):
    location = models.CharField(max_length=200, unique=True)
    sponsor_name = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('location'),
        FieldPanel('sponsor_name'),
        FieldPanel('url'),
        FieldPanel('logo'),
    ]

    def __str__(self):
        return '{} - {}'.format(self.location, self.sponsor_name)
