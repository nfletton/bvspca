from io import BytesIO

import PIL.Image
import pytest
from django.core.files.images import ImageFile
from django.utils import timezone
from wagtail.core.models import Page
from wagtail.images import get_image_model

from bvspca.animals.models import Animal

Image = get_image_model()


def get_test_image_file_jpeg(filename='test.jpg', colour='white', size=(640, 480)):
    f = BytesIO()
    image = PIL.Image.new('RGB', size, colour)
    image.save(f, 'JPEG')
    return ImageFile(f, name=filename)


@pytest.mark.django_db(transaction=False)
def test_social_media_post_not_ready():
    """
    Test that when an animal does not have all the data necessary
    for a social media post, Animal.social_media_ready_to_post()
    returns false
    """
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
    animal_pk = animal.pk
    animal = Animal.objects.get(pk=animal_pk)
    assert not animal.social_media_ready_to_post()


@pytest.mark.django_db(transaction=False)
def test_social_media_adoption_ready_to_post():
    """
    Test that when an animal is in the adopted state (i.e. adoption
    date is set), has a main photo and has an adoption message,
    Animal.social_media_ready_to_post() returns true
    """
    test_image = Image.objects.create(
        title="Test image",
        file=get_test_image_file_jpeg(),
    )
    parent_page = Page.objects.get(url_path='/home/')
    animal = Animal(
        title='Test Animal',
        petpoint_id=123,
        sex='female',
        age=24,
        size='M',
        adoption_date=timezone.now(),
        adoption_message='Great news, today Test Animal was adopted',
        main_photo=test_image,
    )
    parent_page.add_child(instance=animal)
    animal.save()
    animal_pk = animal.pk
    animal = Animal.objects.get(pk=animal_pk)
    assert animal.social_media_ready_to_post()
    assert animal.social_media_post_text() == 'Great news, today Test Animal was adopted'
    assert animal.social_media_post_image() == test_image


@pytest.mark.django_db(transaction=False)
def test_social_media_new_arrival_ready_to_post():
    """
    Test that when an animal is available for adoption, has a main photo and an
    adoption message, Animal.social_media_ready_to_post() returns true
    """
    test_image = Image.objects.create(
        title="Test image",
        file=get_test_image_file_jpeg(),
    )
    parent_page = Page.objects.get(url_path='/home/')
    animal = Animal(
        title='Test Animal',
        petpoint_id=123,
        sex='female',
        age=24,
        size='M',
        description='Great news, Test Animal arrived today',
        main_photo=test_image,
    )
    parent_page.add_child(instance=animal)
    animal.save()
    animal_pk = animal.pk
    animal = Animal.objects.get(pk=animal_pk)
    assert animal.social_media_ready_to_post()
    assert animal.social_media_post_text() == 'Great news, Test Animal arrived today'
    assert animal.social_media_post_image() == test_image
