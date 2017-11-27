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


@register.inclusion_tag('core/tags/meta_tags.html', takes_context=True)
def seo_and_social_meta_tags(context, page):
    site_short_name = getattr(settings, 'SPCA_SITE_SHORT_NAME')
    if hasattr(page, 'seo_and_social_meta_values'):
        request = context.request
        data = page.seo_and_social_meta_values()
        data['root_url'] = '{}://{}'.format(request.scheme, request.META['HTTP_HOST'])
    else:
        data = dict(
            title='{} | {}'.format(page.seo_title if page.seo_title else page.title, site_short_name),
            description=page.search_description,
        )
    return data
