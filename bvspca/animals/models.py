from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

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
        FieldPanel('title'),
        MultiFieldPanel(
            [
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
            ],
            heading="PetPoint Data",
            classname="collapsible collapsed"
        ),
    ]

    @classmethod
    def create(cls, petpoint_data):
        kwargs = {
            'petpoint_id': int(petpoint_data.ID),
            'title': petpoint_data.AnimalName,
            'species': petpoint_data.Species,
            'sex': petpoint_data.Sex,
            'primary_breed': petpoint_data.PrimaryBreed,
            'secondary_breed': petpoint_data.SecondaryBreed,
            'primary_color': petpoint_data.PrimaryColor,
            'secondary_color': petpoint_data.SecondaryColor,
            'age': int(petpoint_data.Age),
            'size': petpoint_data.Size,
            'description': petpoint_data.Dsc,
            'photo_1_url': petpoint_data.Photo1,
            'photo_2_url': petpoint_data.Photo2,
            'photo_3_url': petpoint_data.Photo3,
            'on_hold': True if petpoint_data.OnHold == 'Yes' else False,
            'special_needs': petpoint_data.SpecialNeeds,
            'no_dogs': True if petpoint_data.NoDogs == 'Y' else False,
            'no_cats': True if petpoint_data.NoCats == 'Y' else False,
            'no_kids': True if petpoint_data.NoKids == 'Y' else False,
            'lived_with_kids': petpoint_data.LivedWithChildren,
            'lived_with_animals': petpoint_data.LivedWithAnimals,
            'lived_with_animal_types': petpoint_data.LivedWithAnimalTypes,
            'weight': petpoint_data.BodyWeight,
        }
        return cls(**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        pass


class AnimalsPage(Page, MenuTitleable):
    content_panels = [
        FieldPanel('title'),
    ]

    promote_panels = Page.promote_panels + [FieldPanel('menu_title')]

    def __str__(self):
        return self.title
