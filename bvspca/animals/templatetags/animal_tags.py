from django import template

from bvspca.animals.models import LocationSponsor

register = template.Library()


@register.filter
def to_years_and_months(months):
    """
    Convert a integer value into a string of years and months e.g.
    27 would be represented as '2 Years 3 Months'
    """
    whole_years = months // 12
    remaining_months = months % 12
    result = ''
    if whole_years >= 1:
        if whole_years == 1:
            result = '1 Year '
        else:
            result = '{} Years '.format(whole_years)
    if remaining_months >= 1:
        if months == 1:
            result += '1 Month'
        else:
            result += '{} Months'.format(remaining_months)
    return result


@register.filter
def to_friendly_size(size_code):
    if size_code == 'S':
        return 'Small'
    if size_code == 'M':
        return 'Medium'
    if size_code == 'L':
        return 'Large'
    if size_code == 'XL':
        return 'Extra Large'
    return size_code


@register.inclusion_tag('animals/sponsor.html')
def location_sponsor(animal):
    try:
        sponsor = LocationSponsor.objects.get(location=animal.sub_location)
    except LocationSponsor.DoesNotExist:
        sponsor = None
    return {'sponsor': sponsor, 'animal': animal}

