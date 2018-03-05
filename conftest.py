import pytest
from wagtail.core.models import Page, Site

from bvspca.animals.models import AnimalCountSettings


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        root_page = Page(title='test', path='test', depth=1)
        root_page.save()
        site = Site(hostname='www.example.com', root_page=root_page)
        site.save()
        count_settings = AnimalCountSettings(site_id=site.id)
        count_settings.save()

