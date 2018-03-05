import datetime

import pytest
from django.core.management import call_command
from lxml import etree
from wagtail.wagtailcore.models import Page

from bvspca.animals.petpoint import extract_animal_ids, extract_animal, extract_animal_adoption_dates
from bvspca.animals.models import Animal


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'bvspca/animals/tests/data/test_pages.json')


def test_extract_animal_ids():
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_search_valid_response.xml')
    animal_ids = extract_animal_ids(animal_etree)
    assert len(animal_ids) == 29
    assert animal_ids[0] == 36607476
    assert animal_ids[-1] == 36917491


def test_extract_animal_details():
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_valid_response.xml')
    animal_details = extract_animal(animal_etree)
    assert animal_details.AnimalName == 'Sniffy'
    assert animal_details.DateOfSurrender == datetime.date(2017, 9, 20)


@pytest.mark.django_db(transaction=False)
def test_create_animal_from_petpoint_data():
    animal = create_animal_object()

    retrieved_animal = Animal.objects.get(pk=animal.pk)
    assert retrieved_animal.petpoint_id == 36607476


@pytest.mark.django_db(transaction=False)
def test_update_animal_from_petpoint_data():
    animal = create_animal_object()

    animal = Animal.objects.get(petpoint_id=animal.petpoint_id)
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_valid_modified_response.xml')
    animal_details = extract_animal(animal_etree)
    animal.updateAdoptableAnimal(animal_details)

    retrieved_animal = Animal.objects.get(pk=animal.pk)
    assert retrieved_animal.title == 'Sniffy 2'
    assert retrieved_animal.species == 'Dog'
    assert retrieved_animal.sex == 'Female'
    assert retrieved_animal.primary_breed == 'Domestic Longhair'
    assert retrieved_animal.secondary_breed == 'Mix 2'
    assert retrieved_animal.primary_color == 'Orange'
    assert retrieved_animal.secondary_color == 'Brown'
    assert retrieved_animal.age == 160
    assert retrieved_animal.size == 'M'
    assert retrieved_animal.description == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    assert retrieved_animal.photo_1_url == 'http://www.example.com/1.jpg'
    assert retrieved_animal.photo_2_url == 'http://www.example.com/2.jpg'
    assert retrieved_animal.photo_3_url == 'http://www.example.com/3.jpg'
    assert retrieved_animal.on_hold
    assert retrieved_animal.special_needs == 'special needs'
    assert retrieved_animal.no_dogs
    assert not retrieved_animal.no_cats
    assert retrieved_animal.no_kids
    assert retrieved_animal.lived_with_kids == 'No'
    assert retrieved_animal.lived_with_animals == 'Unknown'
    assert retrieved_animal.lived_with_animal_types == 'snakes'
    assert retrieved_animal.weight == '2 kilograms'
    assert retrieved_animal.surrender_date == datetime.date(2017, 11, 11)


@pytest.mark.django_db(transaction=False)
def test_update_previously_adoptable_animal_from_petpoint_data():
    animal = create_animal_object()
    animal.live = False
    animal.save()

    animal = Animal.objects.get(petpoint_id=animal.petpoint_id)
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_valid_modified_response.xml')
    animal_details = extract_animal(animal_etree)
    animal.updateAdoptableAnimal(animal_details)

    retrieved_animal = Animal.objects.get(pk=animal.pk)
    assert retrieved_animal.live


def test_extract_animal_adoption_dates():
    adoptions_etree = etree.parse('bvspca/animals/tests/data/petpoint_adoptions_valid_response.xml')
    animal_adoptions = extract_animal_adoption_dates(adoptions_etree)
    assert len(animal_adoptions) == 4
    assert animal_adoptions[0][0] == 36917491
    assert animal_adoptions[0][1] == datetime.date(2017, 12, 23)
    assert animal_adoptions[1][0] == 37395336
    assert animal_adoptions[1][1] == datetime.date(2017, 12, 23)
    assert animal_adoptions[-1][0] == 36744898
    assert animal_adoptions[-1][1] == datetime.date(2017, 12, 24)


def test_extract_animal_adoption_dates_when_none():
    adoptions_etree = etree.parse('bvspca/animals/tests/data/petpoint_adoptions_valid_empty_response.xml')
    animal_adoptions = extract_animal_adoption_dates(adoptions_etree)
    assert len(animal_adoptions) == 0


def create_animal_object():
    parent_page = Page.objects.get(url_path='/home/')
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_valid_response.xml')
    animal_details = extract_animal(animal_etree)
    animal = Animal.create(animal_details)
    parent_page.add_child(instance=animal)
    return animal
