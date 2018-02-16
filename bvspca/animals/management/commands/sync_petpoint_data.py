import datetime
import logging

from django.core.management.base import BaseCommand
from zeep import Client

from bvspca.animals.models import Animal, AnimalCountSettings, AnimalsPage
from bvspca.animals.petpoint import fetch_petpoint_adoptable_animal_ids, fetch_petpoint_adopted_dates_since, \
    fetch_petpoint_animal
from bvspca.social.interface import add_to_social_queue

logger = logging.getLogger('bvspca.animals.petpoint')


class Command(BaseCommand):
    help = 'Synchronize data from PetPoint with local Animal objects'

    def handle(self, *args, **options):
        client = Client('http://ws.petango.com/webservices/wsadoption.asmx?WSDL')
        client.raw_response = True

        # create and update animals based on currently adoptable animals
        adoptable_animal_ids = fetch_petpoint_adoptable_animal_ids(client)
        if adoptable_animal_ids is not None:
            for animal_id in adoptable_animal_ids:
                petpoint_animal = fetch_petpoint_animal(client, animal_id)
                if petpoint_animal is not None:
                    try:
                        local_animal = Animal.objects.get(petpoint_id=animal_id)
                        if local_animal.update(petpoint_animal):
                            logger.info(
                                'Updated animal {} ({})'.format(
                                    local_animal.petpoint_id,
                                    local_animal.title,
                                )
                            )
                    except Animal.DoesNotExist:
                        new_animal = Animal.create(petpoint_animal)
                        self.increment_animal_count(new_animal.species, 'rescued')
                        animal_parent = AnimalsPage.objects.get(species=new_animal.species)
                        animal_parent.add_child(instance=new_animal)
                        add_to_social_queue(new_animal)
                        logger.info(
                            'Created animal {} ({})'.format(
                                new_animal.petpoint_id,
                                new_animal.title,
                            )
                        )

        # check for adoptions since yesterday and set adoption dates
        adoptions = fetch_petpoint_adopted_dates_since(client, datetime.date.today() - datetime.timedelta(10))
        if adoptions:
            for adoption in adoptions:
                try:
                    local_animal = Animal.objects.get(petpoint_id=adoption[0])
                    if local_animal.adoption_date != adoption[1]:
                        local_animal.adoption_date = adoption[1]
                        local_animal.live = True
                        local_animal.save()
                        self.increment_animal_count(local_animal.species, 'adopted')
                        add_to_social_queue(local_animal)
                        logger.info(
                            'Animal {} adopted on {}'.format(
                                adoption[0],
                                adoption[1],
                            )
                        )
                except Animal.DoesNotExist:
                    logger.error(
                        'Animal {} did not exist when attempting to set adoption date'.format(
                            adoption[0],
                            adoption[1],
                        )
                    )

        # unpublish animals no longer adoptable yet have not been adopted
        if adoptable_animal_ids is not None:
            unavailable_animals = Animal.objects.filter(live=True, adoption_date__isnull=True).exclude(
                petpoint_id__in=adoptable_animal_ids,
            )
            for animal in unavailable_animals:
                animal.live = False
                animal.save()
                logger.warning(
                    'Unpublished animal {} ({}) because it is neither adoptable or adopted'.format(
                        animal.petpoint_id,
                        animal.title,
                    )
                )

    def increment_animal_count(self, species, event_type):
        """
        Increment the counts of animals rescued and adopted.

        :param species: 'cat' or 'dog'
        :param event_type: 'rescued' or 'adopted'
        :return:
        """
        try:
            animal_counts = AnimalCountSettings.objects.get(site_id=2)
            count_field_name = '{}_{}'.format(species.lower(), event_type.lower())
            current_count = getattr(animal_counts, count_field_name, 0)
            setattr(animal_counts, count_field_name, current_count + 1)
            animal_counts.save()
            logger.info(
                '{} {} count incremented'.format(species, event_type)
            )
        except AnimalCountSettings.DoesNotExist:
            logger.error('Animal count settings do not exist')
