import io
import logging

from django.conf import settings
from lxml import etree

PETPOINT_AUTH_KEY = getattr(settings, 'PETPOINT_AUTH_KEY', "")

logger = logging.getLogger('bvspca.animals.petpoint')
error_logger = logging.getLogger('bvspca.animals.petpoint.errors')


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
    return PetPointAnimal(details)


def fetch_petpoint_animal(client, animal_id):
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


class PetPointAnimal:
    def __init__(self, element):
        self.element = element

    def __getattr__(self, propName):
        property_element = self.element.find(propName)
        if property_element is not None:
            property_value = property_element.text
            if propName in ['ID', 'Age']:
                return int(property_value)
            if propName in ['NoDogs', 'NoCats', 'NoKids']:
                return True if property_value == 'Y' else False
            if propName in ['OnHold']:
                return True if property_value == 'Yes' else False
            if property_value is None:
                return ''
            return property_value
        raise AttributeError('AdoptableAnimal has no attribute {}'.format(propName))
