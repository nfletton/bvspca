from django.db import models
from django.db.models import ForeignKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailsearch import index

from bvspca.core.blocks import ContentStreamBlock
from bvspca.core.models_abstract import MenuTitleable


class Animal(Page):
    # PetPoint read-only fields
    petpoint_id = models.PositiveIntegerField(
        verbose_name='petpoint animal id',
        unique=True,
    )
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
    )
    updates = StreamField(
        ContentStreamBlock(), verbose_name="Animal Updates", blank=True
    )
    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('primary_breed'),
        index.SearchField('secondary_breed'),
        index.SearchField('primary_color'),
        index.SearchField('secondary_color'),
        index.SearchField('size'),
        index.SearchField('description'),
    ]

    subpage_types = []

    content_panels = [
        ImageChooserPanel('main_photo'),
        StreamFieldPanel('additional_photos'),
        StreamFieldPanel('updates'),
        MultiFieldPanel(
            [
                FieldPanel('title'),
                FieldPanel('petpoint_id'),
                FieldPanel('species'),
                FieldPanel('sex'),
                FieldPanel('primary_breed'),
                FieldPanel('secondary_breed'),
                FieldPanel('primary_color'),
                FieldPanel('secondary_color'),
                FieldPanel('age'),
                FieldPanel('size'),
                FieldPanel('description'),
                FieldPanel('photo_1_url'),
                FieldPanel('photo_2_url'),
                FieldPanel('photo_3_url'),
                FieldPanel('on_hold'),
                FieldPanel('special_needs'),
                FieldPanel('no_dogs'),
                FieldPanel('no_cats'),
                FieldPanel('no_kids'),
                FieldPanel('lived_with_kids'),
                FieldPanel('lived_with_animals'),
                FieldPanel('lived_with_animal_types'),
                FieldPanel('weight'),
                FieldPanel('surrender_date'),
                FieldPanel('last_intake_date'),
            ],
            heading="PetPoint Data",
            classname="collapsible collapsed"
        ),
    ]

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
        }

    def update(self, petpoint_data):
        dirty = False
        field_map = self.map_fields(petpoint_data)
        for field_name, value in field_map.items():
            if getattr(self, field_name) != value:
                setattr(self, field_name, value)
                dirty = True
        if petpoint_data.Stage == 'Available' and not self.live:
            self.live = True
            dirty = True
        if dirty:
            self.save()
            return True
        return False

    def __str__(self):
        return self.title

    class Meta:
        pass


class AnimalsPage(Page, MenuTitleable):
    PETPOINT_CAT_CODE = 'Cat'
    PETPOINT_DOG_CODE = 'Dog'
    ANIMAL_TYPES = ((PETPOINT_CAT_CODE, PETPOINT_CAT_CODE), (PETPOINT_DOG_CODE, PETPOINT_DOG_CODE))
    species = models.CharField(max_length=20, choices=ANIMAL_TYPES)
    content_panels = [
        FieldPanel('title'),
        FieldPanel('species'),
    ]

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    def animals(self):
        return Animal.objects.live().descendant_of(self).order_by('-last_intake_date')

    def __str__(self):
        return self.title
