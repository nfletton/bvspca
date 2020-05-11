import datetime
import io
import logging
import html

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
    with client.settings(raw_response=True):
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


def extract_animal_adoption_dates(adoptions_etree):
    """
    Extract animal ids and adoption dates from etree response for
    PetPoints AdoptionList API call

    :param adoptions_etree:
    :return: a list of animal id and adoption date tuples
    """
    animal_adoptions = []
    for adoption in adoptions_etree.findall('.//adoption'):
        id = adoption.find('AnimalID')
        adoption_date = adoption.find('AdoptionDate')
        if id is not None:
            animal_adoptions.append(
                (
                    int(id.text),
                    datetime.datetime.strptime(adoption_date.text[:10], '%Y-%m-%d').date()
                )
            )
    return animal_adoptions


def fetch_petpoint_adopted_dates_since(client, start_date):
    """
    From the start date, retrieve all adopted animals

    :param client: lxml client object
    :param start_date: the date to start checking for adoptions
    :return: a list of animal id and adoption date tuples
    """
    one_day_delta = datetime.timedelta(days=1)
    loop_date = start_date
    end_date = datetime.date.today()
    all_adoptions = []
    while loop_date <= end_date:
        with client.settings(raw_response=True):
            adoption_list_response = client.service.AdoptionList(
                PETPOINT_AUTH_KEY,
                loop_date,                       # adoptionDate
                0,                               # sideID
            )
            if adoption_list_response.status_code is 200:
                all_adoptions.extend(extract_animal_adoption_dates(etree.parse(io.BytesIO(adoption_list_response.content))))
            else:
                error_logger.error(
                    'Failed to retrieve adopted animals for day {}. HTTP status code {}'.format(
                        loop_date,
                        adoption_list_response.status_code,
                    )
                )
            loop_date += one_day_delta
    return all_adoptions


def extract_animal(animal_detail_etree):
    details = animal_detail_etree.find('.//adoptableDetails')
    return PetPointAnimal(details)


def fetch_petpoint_animal(client, animal_id):
    with client.settings(raw_response=True):
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
            if propName in ['DateOfSurrender', 'LastIntakeDate']:
                return datetime.datetime.strptime(property_value[:10], '%Y-%m-%d').date()
            if propName in ['NoDogs', 'NoCats', 'NoKids']:
                return True if property_value == 'Y' else False
            if propName in ['OnHold']:
                return True if property_value == 'Yes' else False
            if property_value is None:
                return ''
            return html.unescape(property_value)
        return None
