from django import template
from django.conf import settings

register = template.Library()


@register.filter
def to_css_name(value):
    return value.lower().replace(' ', '-')


@register.filter
def get_property(instance, key):
    return getattr(instance, key)


@register.simple_tag
def get_addthis_pub_id():
    return getattr(settings, 'ADDTHIS_PUB_ID', "")


@register.simple_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")


@register.simple_tag
def get_google_analytics_id():
    return getattr(settings, 'GOOGLE_ANALYTICS_ID', "")
