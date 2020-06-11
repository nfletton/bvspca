import datetime
import html
import io
import logging

from lxml import etree

logger = logging.getLogger('bvspca.animals.petpoint')
error_logger = logging.getLogger('bvspca.animals.petpoint.errors')


def extract_animal_ids(animal_summary_etree):
    animal_ids = []
    for animal in animal_summary_etree.findall('.//adoptableSearch'):
        id = animal.find('ID')
        if id is not None:
            animal_ids.append(int(id.text))
    return animal_ids


def fetch_petpoint_adoptable_animal_ids(session, base_url):
    params = {
        'speciesID': 0,
        'sex': 'All',
        'ageGroup': 'All',
        'location': '',
        'site': 0,
        'onHold': 'A',
        'orderBy': 'ID',
        'primaryBreed': '',
        'secondaryBreed': '',
        'SpecialNeeds': 'A',
        'noDogs': 'A',
        'noCats': 'A',
        'noKids': 'A',
        'stageID': '',
    }
    adoptable_search_response = session.get(base_url.format('AdoptableSearch'), params=params)
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


def fetch_petpoint_adopted_dates_since(session, base_url, start_date):
    """
    From the start date, retrieve all adopted animals

    :param session: requests session object
    :param base_url: base url of petpoint services
    :param start_date: the date to start checking for adoptions
    :return: a list of animal id and adoption date tuples
    """
    one_day_delta = datetime.timedelta(days=1)
    loop_date = start_date
    end_date = datetime.date.today()
    all_adoptions = []
    while loop_date <= end_date:
        params = {
            'adoptionDate': loop_date,
            'siteID': '',
        }
        adoption_list_response = session.get(base_url.format('AdoptionList'), params=params)
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
    return PetPointAnimal(animal_detail_etree)


def fetch_petpoint_animal(session, base_url, animal_id):
    params = {
        'animalID': animal_id,
    }
    animal_details_response = session.get(base_url.format('AdoptableDetails'), params=params)
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
            property_value = property_element.text.strip()
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
