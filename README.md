# Bow Valley SPCA Website

## Apps

### core

### animals
All animal related data, templates and functionality. The app includes:

* a management command to synchronize animal data managed in 
  PetPoint (http://www.petpoint.com/) with local animal data in this 
  app.
* 

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
### Evironment Variables
The following environment variables need to be set in a production
environment

| Name | Example | Note |
|---|---|---|
| DJANGO_SECRET_KEY | | |
| DJANGO_SETTINGS_MODULE | config.settings.production | |
| DJANGO_ADMIN_URL | r'my-secret-django-admin-path' | Defaults to 'djadmin' in development |
| DATABASE_URL | | |
| WAGTAIL_ADMIN_URL | r'my-secret-wagtail-admin-path' | Defaults to 'admin' in development |
| RECAPTCHA_SITE_KEY | | |
| RECAPTCHA_SECRET_KEY | | |
| GOOGLE_ANALYTICS_ID | | |
| ADDTHIS_PUB_ID  | | |
| MAILCHIMP_USERNAME | | Required by 'newsletter' app |
| MAILCHIMP_SECRET_KEY  | | Required by 'newsletter' app |
| MAILCHIMP_LIST_ID| 83c4276af1 | MailChimp list ID that newsletter will be distributed to |
| MAILCHIMP_TEMPLATE_ID| 351313 | MailChimp template ID that newsletter will be created with |
| MAILCHIMP_SUBJECT| | Subject line of email |
| MAILCHIMP_FROM_NAME| | From name of email |
| MAILCHIMP_REPLY_TO| | Reply to address of email |

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

## Manage.py Cron Jobs

* clearsessions (daily)
* publish_scheduled_pages (hourly)

## Graphic Design

### Fonts
