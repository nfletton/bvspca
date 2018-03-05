import pytest
from wagtail.wagtailcore.models import Page, Site

from bvspca.animals.management.commands.sync_petpoint_data import Command
from bvspca.animals.models import AnimalCountSettings


@pytest.fixture(scope="module")
def animal_settings():
    root_page = Page(title='test', path='test', depth=1)
    root_page.save()
    site = Site(hostname='www.example.com', root_page=root_page)
    site.save()
    count_settings = AnimalCountSettings(site_id=site.id)
    count_settings.save()
    return count_settings


@pytest.mark.django_db(transaction=False)
def test_increment_animal_count(animal_settings):
    for _ in range(1, 100):
        Command.increment_animal_count('Cat', 'adopted')
        animal_settings.refresh_from_db()
    assert animal_settings.cats_adopted == 99
    for _ in range(1, 10):
        Command.increment_animal_count('Cat', 'rescued')
        animal_settings.refresh_from_db()
    assert animal_settings.cats_rescued == 9
    for _ in range(1, 200):
        Command.increment_animal_count('Dog', 'adopted')
        animal_settings.refresh_from_db()
    assert animal_settings.dogs_adopted == 199
    for _ in range(1, 50):
        Command.increment_animal_count('Dog', 'rescued')
        animal_settings.refresh_from_db()
    assert animal_settings.dogs_rescued == 49


@pytest.mark.django_db(transaction=False)
def test_decrement_animal_count(animal_settings):
    animal_settings.cats_adopted = 22
    animal_settings.cats_rescued = 44
    animal_settings.dogs_adopted = 55
    animal_settings.dogs_rescued = 66
    animal_settings.save()

    Command.increment_animal_count('Cat', 'adopted', -1)
    animal_settings.refresh_from_db()
    assert animal_settings.cats_adopted == 21
    Command.increment_animal_count('Dog', 'rescued', -1)
    animal_settings.refresh_from_db()
    assert animal_settings.dogs_rescued == 65
