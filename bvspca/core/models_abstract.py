from django.conf import settings
from django.core.mail import EmailMessage
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


class SendMailMixin:
    def send_mail(self, form):
        addresses = [x.strip() for x in self.to_address.split(',')]
        if not self.from_address:
            if hasattr(settings, 'WAGTAILADMIN_NOTIFICATION_FROM_EMAIL'):
                self.from_address = settings.WAGTAILADMIN_NOTIFICATION_FROM_EMAIL
            elif hasattr(settings, 'DEFAULT_FROM_EMAIL'):
                self.from_address = settings.DEFAULT_FROM_EMAIL
            else:
                self.from_address = 'webmaster@localhost'
        content = []
        for field in form:
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content.append('{}: {}'.format(field.label, value))
        content = '\n'.join(content)
        email = EmailMessage(
            self.subject,
            content,
            self.from_address,
            addresses,
            [],
            reply_to=[form.cleaned_data['email']] if form.cleaned_data.get('email', False) else None,
        )
        email.send()

    class Meta:
        abstract = True
