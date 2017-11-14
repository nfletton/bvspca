import logging

from django.core.management.base import BaseCommand
from zeep import Client

from bvspca.animals.models import Animal, AnimalsPage
from bvspca.animals.petpoint import fetch_petpoint_adoptable_animal_ids, fetch_petpoint_animal

logger = logging.getLogger('bvspca.animals.petpoint')


class Command(BaseCommand):
    help = 'Synchronize animal data from PetPoint'

    def handle(self, *args, **options):
        client = Client('http://ws.petango.com/webservices/wsadoption.asmx?WSDL')
        client.raw_response = True

        adoptable_animal_ids = fetch_petpoint_adoptable_animal_ids(client)
        if adoptable_animal_ids is not None:
            animal_parent = AnimalsPage.objects.get(pk=13)
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
                        animal_parent.add_child(instance=new_animal)
                        logger.info(
                            'Created animal new {} ({})'.format(
                                new_animal.petpoint_id,
                                new_animal.title,
                            )
                        )
            # unpublish animals no longer adoptable
            Animal.objects.filter(live=True).exclude(petpoint_id__in=adoptable_animal_ids).update(live=False)

