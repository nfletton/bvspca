import logging
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from mailchimp3 import MailChimp
from wagtail.core.models import Site

from bvspca.animals.models import Animal


class Command(BaseCommand):
    help = 'Send weekly update email'

    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        client = MailChimp(settings.MAILCHIMP_SECRET_KEY, settings.MAILCHIMP_USERNAME,  timeout=20.0)

        campaign_data = {
            "type": "regular",
            "recipients": {
                "list_id": settings.MAILCHIMP_LIST_ID,
            },
            "settings": {
                "subject_line": settings.MAILCHIMP_SUBJECT,
                "title": '{} ({:%Y-%m-%d})'.format(settings.MAILCHIMP_SUBJECT, datetime.date.today()),
                "from_name": settings.MAILCHIMP_FROM_NAME,
                "reply_to": settings.MAILCHIMP_REPLY_TO,
                "template_id": int(settings.MAILCHIMP_TEMPLATE_ID),
            },
        }
        try:
            campaign = client.campaigns.create(campaign_data)
        except Exception as e:
            self.logger.error('Failed to create MailChimp weekly update campaign: %s', e)
            raise

        try:
            since_date = datetime.date.today() - datetime.timedelta(14)
            site = Site.objects.get(pk=2)
            site_url = site.root_url
            content = {
                'template': {
                    'id': int(settings.MAILCHIMP_TEMPLATE_ID),
                    'sections': {
                        'arrived': self.new_animals_list(since_date, site_url),
                        'adopted': self.adopted_animals_list(since_date, site_url),
                    },
                },
            }
        except Exception as e:
            self.logger.error('Failed to prepared date for weekly animal update')
            raise

        try:
            client.campaigns.content.update(campaign['id'], content)
        except Exception as e:
            self.logger.error('Failed to update MailChimp campaign (%s) with content: %s', campaign['id'], e)
            raise

        try:
            response = client.campaigns.actions.send(campaign['id'])
            if response:
                self.logger.error('%s', response)
        except Exception as e:
            self.logger.error('Failed to send MailChimp campaign (%s): %s', campaign['id'], e)

    @staticmethod
    def new_animals_list(since, root_url):
        new_animals = Animal.objects\
            .filter(adoption_date__isnull=True, last_intake_date__gte=since)\
            .live()\
            .order_by('last_intake_date')
        if new_animals:
            return render_to_string(
                'newsletter/animal_list.html',
                {'animals': new_animals, 'root_url': root_url}
            )
        else:
            return '<p class="animal-news__empty">No new animals for this period</p>'

    @staticmethod
    def adopted_animals_list(since, root_url):
        adopted_animals = Animal.objects.filter(adoption_date__gte=since).live().order_by('adoption_date')
        if adopted_animals:
            return render_to_string(
                'newsletter/animal_list.html',
                {'animals': adopted_animals, 'root_url': root_url}
            )
        else:
            return '<p class="animal-news__empty">No adopted animals for this period</p>'
