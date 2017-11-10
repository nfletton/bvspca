import io
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from lxml import etree
from zeep import Client

PETPOINT_AUTH_KEY = getattr(settings, 'PETPOINT_AUTH_KEY', "")


class Command(BaseCommand):
    help = 'Synchronize animal data from PetPoint'

    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        client = Client('http://ws.petango.com/webservices/wsadoption.asmx?WSDL')
        client.raw_response = True

        adoptable_animal_ids = fetch_petpoint_adoptable_animal_ids(client)

        for animal_id in adoptable_animal_ids:
            animal_details = fetch_petpoint_animal_details(client, animal_id)
            print(animal_details.AnimalName)


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
    return extract_animal_ids(etree.parse(io.BytesIO(adoptable_search_response.content)))


def extract_animal(animal_detail_etree):
    details = animal_detail_etree.find('.//adoptableDetails')
    return AdoptableAnimal(details)


def fetch_petpoint_animal_details(client, animal_id):
    animal_details_response = client.service.AdoptableDetails(
        animal_id,
        PETPOINT_AUTH_KEY,
    )
    return extract_animal(etree.parse(io.BytesIO(animal_details_response.content)))


class AdoptableAnimal:
    def __init__(self, element):
        self.element = element

    def __getattr__(self, item):
        property_element = self.element.find(item)
        if property_element is not None:
            return property_element.text
        raise AttributeError('AdoptableAnimal has no attribute {}'.format(item))
