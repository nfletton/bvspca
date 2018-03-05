import pytest

from bvspca.animals.management.commands.sync_petpoint_data import Command
from bvspca.animals.models import AnimalCountSettings


@pytest.mark.django_db
def test_decrement_animal_count():
    animal_settings = AnimalCountSettings.objects.get(pk=1)
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


@pytest.mark.django_db
def test_increment_animal_count():
    animal_settings = AnimalCountSettings.objects.get(pk=1)
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
