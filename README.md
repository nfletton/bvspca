# Bow Valley SPCA Website

The Bow Valley SPCA's mission is to provide the community with an 
adoption centre following a no kill, no cage philosophy to shelter, 
care for and re-home stray and abandoned dogs and cats and promote 
humane attitudes and responsible pet companionship through educational 
programs and community leadership.

Sponsorship of the website build has been provided by the
[Calgary Foundation](https://calgaryfoundation.org/) and 
[Blue Hut](https://www.thebluehut.com/). Read more 
[here](https://www.bowvalleyspca.org/credits/)

The code for the website is open source and other SPCAs, in particular,
are encouraged to make use of the code as they see fit.

## Key Website Features

* Easy to use content editing interface
* Supports news, events, team and general content management for the
  centre
* Integrates with [PetPoint](http://www.petpoint.com/) 
  data management system for a feed of adoptable animals at the centre 
* Animal data retrieved from PetPoint is stored locally to the website
  to allow:
    - end-users to interact with animal information directly
      on the website
    - improved social interactions with the website via Facebook, 
      Twitter and email marketing
    - improved SEO
    - ability to allow additional content to be associated with animals
      that is not supported by PetPoint
* Automated posting of new and recently adopted animals to Facebook
  and Twitter
* Automated regular email listing new arrivals and recently adopted 
  animals

## Technical Overview

The website is built with [Wagtail](https://wagtail.io/) and 
[Django](https://www.djangoproject.com/).

Experience with either Django or Wagtail will be required to make use
of this code.

Code structure based on 
[cookiecutter-django](https://github.com/pydanny/cookiecutter-django)


## Django Apps

### core

### animals
The animals app provides the main functionality for displaying animals
available for adoption. The app is based around using 
PetPoint (http://www.petpoint.com/) for managing animal data. It
provides a Django [management command](#cronjobs) to synchronize 
current adoptable animals in the PetPoint data management system 
with an 'Animal' Wagtail page model.

A PETPOINT_AUTH_KEY [environment variable](#venv) needs to be set to
enable access to the PetPoint SOAP API.

Photo galleries on the animal details page use
[Featherlight](https://github.com/noelboss/featherlight/) jQuery 
lightbox plugin.

The animals app can easily be modified for rescue centres
that do not use PetPoint by modifying the Wagtail Animal page model
to suit their specific requirements.


### newsletter
The newsletter app provides a [management command](#cronjobs) to 
construct and send a weekly newsletter listing recently arrived and 
adopten animals. The newsletter is published via MailChimp.

The newsletter includes:

* animals arrived in the last 14 days
* animals adopted in the last 14 days

### social

The social app provides a simple queue where pages can be appended for
later posting to social media. A [management command](#cronjobs) is run
to dequeue items and post them to Facebook and Twitter.

Pages implementing the SocialMediaPostable abstract class can be added 
to the queue. Currently only the Animal page model implements this.

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
| RECAPTCHA_SITE_KEY | | | Google Recaptcha |
| RECAPTCHA_SECRET_KEY | | |  Google Recaptcha |
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
| WAGTAILADMIN_NOTIFICATION_FROM_EMAIL | | | Admin From email |
| FACEBOOK_PAGE_ACCESS_TOKEN | social | | Facebook page access token |
| FACEBOOK_PAGE_ID | social | | Facebook page id |
| TWITTER_CONSUMER_KEY | social | | Twitter consumer key |
| TWITTER_CONSUMER_SECRET | social | | Twitter consumer secret |
| TWITTER_ACCESS_TOKEN_KEY | social | | Twitter access token key |
| TWITTER_ACCESS_TOKEN_SECRET | social | | Twitter access token secret |

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

### Live reloading, Sass compilation and JS bundling

```sh
  $ npm start
```

### Production Sass compilation and JS bundling

```sh
  $ npm run build
```

## <a name="cronjobs"/>Manage.py Cron Jobs Summary

| Command | Required by |Suggested Frequency | Note |
|---|---|---|---|
| clearsessions | django | daily | |
| publish_scheduled_pages | wagtail | every hour | |
| sync_petpoint_data | animals app | every 30 minutes | |
| send_newsletter | newsletter app | weekly | |
| post_social_media | social app | daily | |
