import logging
from datetime import datetime, timedelta

from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from wagtail.models import Page

logger = logging.getLogger('bvspca.social')


class SocialMediaPostable():
    def social_media_post_status(self):
        """
        Status of a page in terms of it's readiness to be posted to social media.
        :return: a list of textual reasons why a page is not ready to be posted to social media
                 or an empty list if the page is ready to be posted
        """
        raise NotImplemented()

    def social_media_post_text(self):
        raise NotImplemented()

    def social_media_post_image(self):
        raise NotImplemented()

    class Meta:
        abstract = True


class SocialMediaQueueManager(models.Manager):
    def delete_old_entries(self):
        """
        Delete all entries from queue older than 28 days

        :return:
        """
        count, counts_by_object_type = self.filter(date__lt=datetime.now() - timedelta(28)).delete()
        if count > 0:
            for object_type, object_count in counts_by_object_type.items():
                logger.info('Deleted {} objects of type {}'.format(object_count, object_type))

    def next_postable_entry(self):
        """
        Get the next queued entry that is ready to post
        :return:
        """
        entries = self.order_by('+priority', '+date')
        for entry in entries:
            if entry.page.ready_to_post():
                return entry


class SocialMediaQueue(models.Model):
    """
    A queue of potential pages to post to social media
    """
    PRIORITIES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    date = models.DateTimeField(verbose_name='timestamp', auto_now_add=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES)
    page = models.OneToOneField(
        Page,
        on_delete=models.DO_NOTHING,
        related_name='+',
    )

    objects = SocialMediaQueueManager()

    class Meta:
        pass

    def status(self):
        status = self.page.specific.social_media_post_status()
        if status:
            return format_html("<span style=\"color:red\">{}</span>", mark_safe('<br>'.join(status)))
        else:
            return format_html('<span style="color:green">Ready to post</span>')

    def page_link(self):
        return format_html('<a href="{}">{}</a>', self.page.get_url(), self.page.title)

    def __str__(self):
        return self.page.title
