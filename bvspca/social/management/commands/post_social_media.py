import logging

from TwitterAPI import TwitterAPI
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.html import strip_tags
from django.utils.text import Truncator
from facebook import GraphAPI

from bvspca.social.models import SocialMediaQueue


class Command(BaseCommand):
    help = 'Post a queued page to social media'

    logger = logging.getLogger('bvspca.social')

    def handle(self, *args, **options):
        queued_entries = SocialMediaQueue.objects.all().order_by('priority', '-date')
        for entry in queued_entries:
            # post first page ready to post
            page_to_post = entry.page.specific
            if hasattr(page_to_post, 'social_media_ready_to_post') and page_to_post.social_media_ready_to_post():
                content = self.prepare_content(page_to_post)
                self.twitter_post(content)
                self.facebook_post(content)
                entry.delete()
                break

    def facebook_post(self, content):
        page_access_token = settings.FACEBOOK_PAGE_ACCESS_TOKEN
        api = GraphAPI(page_access_token)
        # https://developers.facebook.com/docs/graph-api/reference/v2.12/user/feed
        api.put_object(
            parent_object=settings.FACEBOOK_PAGE_ID,
            connection_name="feed",
            message=content['message'],
            link=content['destination'],
        )

    def twitter_post(self, content):
        credentials = {
            'CONSUMER_KEY': settings.TWITTER_CONSUMER_KEY,
            'CONSUMER_SECRET': settings.TWITTER_CONSUMER_SECRET,
            'ACCESS_TOKEN_KEY': settings.TWITTER_ACCESS_TOKEN_KEY,
            'ACCESS_TOKEN_SECRET': settings.TWITTER_ACCESS_TOKEN_SECRET,
        }
        api = TwitterAPI(credentials['CONSUMER_KEY'],
                         credentials['CONSUMER_SECRET'],
                         credentials['ACCESS_TOKEN_KEY'],
                         credentials['ACCESS_TOKEN_SECRET'])
        response = api.request('media/upload', None, {'media': content['image_data']})
        if response.status_code is 200:
            media_id = response.json()['media_id']
            response = api.request(
                'statuses/update',
                {
                    'status': Truncator(content['message']).chars(250) + ' ' + content['destination'],
                    'media_ids': media_id,
                }
            )
            if response.status_code != 200:
                self.logger.error('Twitter post failed for page {}: {}'.format(content['name'], response.text))
        else:
            self.logger.error('Twitter image upload failed for {}: {}'.format(content['image'].title, response.text))

    def prepare_content(self, page):
        page_image = page.social_media_post_image()
        sized_image = page_image.get_rendition('width-1000|jpegquality-90')
        try:
            sized_image.file.open()
            raw_image_data = sized_image.file.read()
            sized_image.file.close()
        except (OSError, IOError) as e:
            self.logger.error('Error creating size restricted rendition of social media image {}'.format(e))
            raise
        else:
            return {
                'message': strip_tags(page.social_media_post_text()),
                'image_data': raw_image_data,
                'image_url': sized_image.url,
                'destination': page.get_full_url(),
                'name': page.title,
            }
