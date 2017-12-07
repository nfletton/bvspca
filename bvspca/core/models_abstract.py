from django.conf import settings
from django.db import models
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class MenuTitleable(models.Model):
    menu_title = models.CharField(verbose_name='menu title', max_length=100, blank=True)

    class Meta:
        abstract = True


class Attachable(models.Model):
    attachments = StreamField([
        ('document', DocumentChooserBlock(icon='fa-file-text')),
    ], blank=True,)

    class Meta:
        abstract = True


class MetaTagable(models.Model):
    def seo_and_social_meta_values(self):
        site_short_name = getattr(settings, 'SPCA_SITE_SHORT_NAME')
        title = self.seo_title if self.seo_title else self.title
        return {
            'title': '{} | {}'.format(title, site_short_name),
            'description': self.search_description,
        }

    class Meta:
        abstract = True
