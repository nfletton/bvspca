from django import template

register = template.Library()


@register.filter
def to_years_an_months(months):
    """
    Convert a integer value into a string of years and months e.g.
    27 would be represented as '2 Years 3 Months'
    """
    whole_years = months // 12
    remaining_months = months % 12
    result = ''
    if whole_years >= 1:
        if whole_years == 1:
            result = '1 Year'
        else:
            result = '{} Years '.format(whole_years)
    if remaining_months >= 1:
        if months == 1:
            result += '1 Month'
        else:
            result += '{} Months '.format(remaining_months)
    return result
