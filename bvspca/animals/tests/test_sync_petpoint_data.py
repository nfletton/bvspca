import pytest
from django.core.management import call_command
from lxml import etree
from wagtail.wagtailcore.models import Page

from bvspca.animals.management.commands.sync_petpoint_data import extract_animal, extract_animal_ids
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


@pytest.mark.django_db(transaction=False)
def test_create_animal_from_petpoint_data():
    parent_page = Page.objects.get(url_path='/home/')
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_valid_response.xml')
    animal_details = extract_animal(animal_etree)
    animal = Animal.create(animal_details)
    parent_page.add_child(instance=animal)

    retrieved_animal = Animal.objects.get(pk=animal.pk)
    assert retrieved_animal.petpoint_id == 36607476
