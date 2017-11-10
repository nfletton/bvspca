from lxml import etree

from bvspca.animals.management.commands.sync_petpoint_data import extract_animal, extract_animal_ids


def test_extract_animal_ids():
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_search_valid_response.xml')
    animal_ids = extract_animal_ids(animal_etree)
    assert len(animal_ids) == 29
    assert animal_ids[0] == 36607476
    assert animal_ids[-1] == 36917491


def test_extract_animal_details():
    animal_etree = etree.parse('bvspca/animals/tests/data/petpoint_animal_valid_response.xml')
    animal_details = extract_animal(animal_etree)
    assert animal_details.AnimalName == 'Sniffy'
