# Bow Valley SPCA Website

## Deployment
### Evironment Variables
The following environment variables need to be set in a production
environment
```
DJANGO_SECRET_KEY
DJANGO_SETTINGS_MODULE = 'config.settings.production'
DATABASE_URL
WAGTAIL_ADMIN_URL = r'my-secret-path'
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
GOOGLE_ANALYTICS_ID 
```

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
