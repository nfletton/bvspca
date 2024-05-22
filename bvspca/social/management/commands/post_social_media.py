import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.html import strip_tags
from facebook import GraphAPI

from bvspca.social.models import SocialMediaQueue


class Command(BaseCommand):
    help = 'Post a queued page to social media'

    logger = logging.getLogger('bvspca.social')

    def handle(self, *args, **options):
        SocialMediaQueue.objects.delete_old_entries()
        queued_entries = SocialMediaQueue.objects.all().order_by('priority', '-date')
        for entry in queued_entries:
            # post first page ready to post
            page_to_post = entry.page.specific
            if hasattr(page_to_post, 'social_media_post_status') and not page_to_post.social_media_post_status():
                content = self.prepare_content(page_to_post)
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
