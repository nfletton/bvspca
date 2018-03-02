import pytest
from wagtail.wagtailcore.models import Site, Page

from bvspca.animals.management.commands.sync_petpoint_data import Command
from bvspca.animals.models import AnimalCountSettings


@pytest.mark.django_db(transaction=False)
def test_increment_animal_count():
    root_page = Page(title='test', path='test', depth=1)
    root_page.save()
    site = Site(hostname='www.example.com', root_page=root_page)
    site.save()
    count_settings = AnimalCountSettings(site_id=site.id)
    count_settings.save()
    for _ in range(1, 100):
        Command.increment_animal_count('Cat', 'adopted')
    count_settings.refresh_from_db()
    assert count_settings.cats_adopted == 99
    for _ in range(1, 10):
        Command.increment_animal_count('Cat', 'rescued')
    count_settings.refresh_from_db()
    assert count_settings.cats_rescued == 9
    for _ in range(1, 200):
        Command.increment_animal_count('Dog', 'adopted')
    count_settings.refresh_from_db()
    assert count_settings.dogs_adopted == 199
    for _ in range(1, 50):
        Command.increment_animal_count('Dog', 'rescued')
    count_settings.refresh_from_db()
    assert count_settings.dogs_rescued == 49
