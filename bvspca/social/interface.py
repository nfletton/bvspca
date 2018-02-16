import logging

from bvspca.social.models import SocialMediaQueue


logger = logging.getLogger('bvspca.social')


def add_to_social_queue(page, priority=3):
    """
    Add the page to the social media queue or if the page is already
    in the queue update the existing entry.

    :param page: the page to be queued
    :param priority: the priority, 1 to 5, of this social media post
    :return: the social media queue entry
    """
    entry, created = SocialMediaQueue.objects.update_or_create(
        page=page,
        defaults={'priority': priority}
    )
    if created:
        logger.info('Page \'{}\'(id: {}) entry created in social media queue'.format(page.title, page.pk))
    else:
        logger.info('Page \'{}\'(id: {}) entry updated in social media queue'.format(page.title, page.pk))
    return entry
