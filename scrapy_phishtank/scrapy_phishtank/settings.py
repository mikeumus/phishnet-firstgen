"""
Django settings for scrapy_phishtank project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from __future__ import absolute_import
# ^^^ The above is required if you want to import from the celery
# library.  If you don't have this then `from celery.schedules import`
# becomes `proj.celery.schedules` in Python 2.x since it allows
# for relative imports by default.

import os

# Celery settings
import djcelery
djcelery.setup_loader()

# http://fearofcode.github.io/blog/2013/01/15/how-to-scrub-sensitive-information-from-django-settings-dot-py-files/
from scrapy_phishtank.settings_secret import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin', # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
    'django.contrib.admindocs', # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/admindocs/
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pishing', # django project app,
    'djcelery', # django-celery module
    'kombu.transport.django.KombuAppConfig', # from celery docs django template: https://github.com/celery/celery/blob/3.1/examples/django/proj/settings.py#L137
    'processes' # Celery app
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'scrapy_phishtank.urls'

WSGI_APPLICATION = 'scrapy_phishtank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',  # path to database file if using sqlite3.
        'USER': '',        # Not used with sqlite3.
        'PASSWORD': '',    # Not used with sqlite3.
        'HOST': '',        # Set to empty string for localhost.
                           # Not used with sqlite3.
        'PORT': '',        # Set to empty string for default.
                           # Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
