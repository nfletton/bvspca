import io
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from lxml import etree
from zeep import Client

from bvspca.animals.models import Animal, AnimalsPage

PETPOINT_AUTH_KEY = getattr(settings, 'PETPOINT_AUTH_KEY', "")

logger = logging.getLogger('bvspca.animals.petpoint')
error_logger = logging.getLogger('bvspca.animals.petpoint.errors')


class Command(BaseCommand):
    help = 'Synchronize animal data from PetPoint'

    def handle(self, *args, **options):
        client = Client('http://ws.petango.com/webservices/wsadoption.asmx?WSDL')
        client.raw_response = True

        adoptable_animal_ids = fetch_petpoint_adoptable_animal_ids(client)
        if adoptable_animal_ids is not None:
            animal_parent = AnimalsPage.objects.get(pk=13)
            for animal_id in adoptable_animal_ids:
                petpoint_animal_details = fetch_petpoint_animal_details(client, animal_id)
                if petpoint_animal_details is not None:
                    try:
                        local_animal_details = Animal.objects.get(petpoint_id=animal_id)
                        # TODO: update existing animal details
                        logger.info(
                            'Updated animal {} ({})'.format(
                                local_animal_details.petpoint_id,
                                local_animal_details.title,
                            )
                        )
                    except Animal.DoesNotExist:
                        new_animal = Animal.create(petpoint_animal_details)
                        animal_parent.add_child(instance=new_animal)
                        logger.info(
                            'Created animal new {} ({})'.format(
                                new_animal.petpoint_id,
                                new_animal.title,
                            )
                        )


def extract_animal_ids(animal_summary_etree):
    animal_ids = []
    for animal in animal_summary_etree.findall('.//adoptableSearch'):
        id = animal.find('ID')
        if id is not None:
            animal_ids.append(int(id.text))
    return animal_ids


def fetch_petpoint_adoptable_animal_ids(client):
    adoptable_search_response = client.service.AdoptableSearch(
        PETPOINT_AUTH_KEY,
        0,  # speciesID
        'All',  # sex
        'All',  # ageGroup
        '',  # location
        0,  # site
        'A',  # onHold
        'ID',  # orderBy
        '',  # primaryBreed
        '',  # secondaryBreed
        'A',  # SpecialNeeds
        'A',  # noDogs
        'A',  # noCats
        'A',  # noKids
        '',  # stageID
    )
    if adoptable_search_response.status_code is 200:
        return extract_animal_ids(etree.parse(io.BytesIO(adoptable_search_response.content)))
    else:
        error_logger.error(
            'Failed to retrieve adoptable animals. HTTP status code {}'.format(
                adoptable_search_response.status_code,
            )
        )


def extract_animal(animal_detail_etree):
    details = animal_detail_etree.find('.//adoptableDetails')
    return AdoptableAnimal(details)


def fetch_petpoint_animal_details(client, animal_id):
    animal_details_response = client.service.AdoptableDetails(
        animal_id,
        PETPOINT_AUTH_KEY,
    )
    if animal_details_response.status_code is 200:
        return extract_animal(etree.parse(io.BytesIO(animal_details_response.content)))
    else:
        error_logger.error(
            'Failed to retrieve animal {} details. HTTP status code: {}. Reason: {}'.format(
                animal_id,
                animal_details_response.status_code,
                animal_details_response.reason,
            )
        )


class AdoptableAnimal:
    def __init__(self, element):
        self.element = element

    def __getattr__(self, item):
        property_element = self.element.find(item)
        if property_element is not None:
            property_value = property_element.text
            if property_value is None:
                return ''
            else:
                return property_value
        raise AttributeError('AdoptableAnimal has no attribute {}'.format(item))
