from datetime import timedelta

import pytest
from django.utils import timezone
from wagtail.core.models import Page

from bvspca.animals.models import Animal
from bvspca.social.interface import add_to_social_queue
from bvspca.social.models import SocialMediaQueue


@pytest.mark.django_db(transaction=False)
def test_add_a_page_to_the_social_media_queue():
    parent_page = Page.objects.get(url_path='/home/')
    animal = Animal(
        title='Test Animal',
        petpoint_id=123,
        sex='female',
        age=24,
        size='M',
    )
    parent_page.add_child(instance=animal)
    animal.save()
    add_to_social_queue(animal, priority=1)
    assert len(SocialMediaQueue.objects.all()) == 1


@pytest.mark.django_db(transaction=False)
def test_add_a_duplicate_page_to_the_social_media_queue():
    parent_page = Page.objects.get(url_path='/home/')
    animal = Animal(
        title='Test Animal',
        petpoint_id=123,
        sex='female',
        age=24,
        size='M',
    )
    parent_page.add_child(instance=animal)
    animal.save()
    add_to_social_queue(animal, priority=1)
    add_to_social_queue(animal, priority=5)
    social_queue = SocialMediaQueue.objects.all()
    assert len(social_queue) == 1
    assert social_queue[0].priority == 5


@pytest.mark.django_db(transaction=False)
def test_delete_old_entries_from_queue():
    parent_page = Page.objects.get(url_path='/home/')
    entries = []
    for i in range(0, 5):
        animal = Animal(
            title='Test Animal',
            petpoint_id=i,
            sex='female',
            age=i * 10,
            size='M',
        )
        parent_page.add_child(instance=animal)
        animal.save()
        entries.append(add_to_social_queue(animal))
    # set date of entries that will be considered old
    entries[0].date = timezone.now() - timedelta(29)
    entries[3].data = timezone.now() - timedelta(41)
    # set date of entries that will be considered current
    entries[1].date = timezone.now() - timedelta(28)
    entries[2].data = timezone.now() - timedelta(6)
    entries[4].data = timezone.now()
    for entry in entries:
        entry.save()
    SocialMediaQueue.objects.delete_old_entries()
    remaining_entries = SocialMediaQueue.objects.all()
    assert len(remaining_entries) == 3
