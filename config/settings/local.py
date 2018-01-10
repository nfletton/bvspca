"""
Local settings

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='+.[(;=Q07q6tB9UblTzVS{k>59g{t/AhOX?@8O$rq=_H%GxGGT')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('wagtail.contrib.wagtailstyleguide', )

ALLOWED_HOSTS = ('127.0.0.1', '10.0.0.101', 'localhost', 'www.dev.bluehut.ca')

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'weekly_emails': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '{}/logs/weekly-email.log'.format(env.str('HOME')),
            'formatter': 'verbose',
        },
        'petpoint': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '{}/logs/petpoint-updates.log'.format(env.str('HOME')),
            'formatter': 'verbose',
        },
        'petpoint-errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '{}/logs/petpoint-errors.log'.format(env.str('HOME')),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'bvspca.newsletter': {
            'level': 'ERROR',
            'handlers': ['weekly_emails'],
            'propagate': False
        },
        'bvspca.animals.petpoint': {
            'level': 'INFO',
            'handlers': ['petpoint'],
            'propagate': False
        },
        'bvspca.animals.petpoint.errors': {
            'level': 'ERROR',
            'handlers': ['petpoint-errors'],
            'propagate': False
        },
    }
}
