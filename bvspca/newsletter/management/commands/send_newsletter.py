import logging
from datetime import date

from django.conf import settings
from django.core.management.base import BaseCommand
from mailchimp3 import MailChimp


class Command(BaseCommand):
    help = 'Send weekly update email'

    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        client = MailChimp(settings.MAILCHIMP_USERNAME, settings.MAILCHIMP_SECRET_KEY, timeout=20.0)

        campaign_data = {
            "type": "regular",
            "recipients": {
                "list_id": settings.MAILCHIMP_LIST_ID,
            },
            "settings": {
                "subject_line": settings.MAILCHIMP_SUBJECT,
                "title": '{} ({:%Y-%m-%d})'.format(settings.MAILCHIMP_SUBJECT, date.today()),
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

        content = {
            'template': {
                'id': int(settings.MAILCHIMP_TEMPLATE_ID),
                'sections': {
                    'body': '<h2>hello world</h2>',
                },
            },
        }
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
