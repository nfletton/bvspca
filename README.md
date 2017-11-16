# Bow Valley SPCA Website

## Apps

### core

### animals
This app provides the main functionality for displaying animals
available for adoption. The app is based around using 
PetPoint (http://www.petpoint.com/) for managing animal data. It
provides a Django [management command](#cronjobs) to synchronize 
current adoptable animals in the PetPoint data management system 
with an 'Animal' Wagtail page model.

A PETPOINT_AUTH_KEY [environment variable](#venv) needs to be set to
enable access to the PetPoint SOAP API.

The animals app can easily be modified for rescue centres
that do not use PetPoint by modifying the Wagtail Animal page model
to suit specific requirements.


### newsletter
Includes a management command to construct a weekly newsletter with
recent updates on animals, news and events. The newsletter is published
via MailChimp.

The newsletter includes:

* animals arrived in the last 14 days
* animals adopted in the last 14 days
* upcoming events in the next 7 days
* news items in the last 7 days


## Deployment
### <a name="venv"/>Evironment Variables
The following environment variables need to be set in a production
environment

| Name | App |Example | Note |
|---|---|---|---|
| DJANGO_SECRET_KEY | | | |
| DJANGO_SETTINGS_MODULE | | config.settings.production | |
| DJANGO_ADMIN_URL | | r'my-secret-django-admin-path' | Defaults to 'djadmin' in development |
| DATABASE_URL | | | |
| WAGTAIL_ADMIN_URL | | r'my-secret-wagtail-admin-path' | Defaults to 'admin' in development |
| RECAPTCHA_SITE_KEY | | | |
| RECAPTCHA_SECRET_KEY | | | |
| GOOGLE_ANALYTICS_ID | core | | |
| ADDTHIS_PUB_ID  | core | | |
| MAILCHIMP_USERNAME | newsletter | | Required by 'newsletter' app |
| MAILCHIMP_SECRET_KEY | newsletter | | Required by 'newsletter' app |
| MAILCHIMP_LIST_ID | newsletter | 83c4276af1 | MailChimp list ID that newsletter will be distributed to |
| MAILCHIMP_TEMPLATE_ID | newsletter | 351313 | MailChimp template ID that newsletter will be created with |
| MAILCHIMP_SUBJECT | newsletter | | Subject line of email |
| MAILCHIMP_FROM_NAME | newsletter | | From name of email |
| MAILCHIMP_REPLY_TO | newsletter | | Reply to address of email |
| PETPOINT_AUTH_KEY | animals | | PetPoint Authorization Key |

## Development Commands

### Code Style Checks

```sh
  $ flake8 bvspca
```

### Tests

```sh
  $ pytest bvspca
  $ pytest bvspca --reuse-db       # reuses the existing test db
  $ pytest bvspca --create-db      # forces the test db to be recreated
  $ pytest bvspca -f               # watches for changes if pytest-xdist installed
```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::
```sh
    $ pytest --cov=bvspca bvspca                              # results in terminal
    $ pytest --cov-report html:htmlcov --cov=bvspca bvspca    # html report to directory htmlcov
```

### Live reloading, Sass compilation and JS bundling

```sh
  $ npm start
```

### Production Sass compilation and JS bundling

```sh
  $ npm run build
```

## <a name="cronjobs"/>Manage.py Cron Jobs Summary

| Command | Required by |Frequency | Note |
|---|---|---|---|
| clearsessions | django | daily | |
| publish_scheduled_pages | wagtail | hourly | |
| sync_petpoint_data | animals app | daily | |
| send_newsletter | newsletter app | weekly | |

## Graphic Design

### Fonts
