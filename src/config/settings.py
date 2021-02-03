import os
import secrets
from pathlib import Path

import dj_database_url

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

try:
    from psycopg2cffi import compat
    compat.register()
except ImportError:
    pass


Truthy = ['True', 'true', '1', 'yes', 'y']
BASE_DIR = Path(__file__).parent.parent
CUR_DIR = Path.cwd()

CLIENT_DIR = BASE_DIR / 'client'

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    # Generate at least 50 characters
    # 38 bytes encodes (via base64) to 51 characters.
    # Without a parameter, this may default to only 44 characters.
    # Increase strength here as necessary.
    SECRET_KEY = secrets.token_urlsafe(38)

DEBUG = os.environ.get('DEBUG', 'False') in Truthy
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
PORT = int(os.environ.get('PORT', '8000'))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_jinja',

    'graphene_django',
    'react_loader',
    'node',

    'blog',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = [
    # Copy files from STATICFILES_DIR
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # Copy files from each django app
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# React generated files
REACT_LOADER_BUNDLE_DIR = CLIENT_DIR / 'build'
STATICFILES_DIRS = (
    # React static files
    CLIENT_DIR / 'build' / 'static',
)

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'DIRS': [],
        'OPTIONS': {
            'match_extension': '.j2',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

GRAPHENE = {
    'SCHEMA': 'blog.schema.schema',
}

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///{}/db.sqlite3'.format(BASE_DIR))
}

CACHE_MIDDLEWARE_SECONDS = 3600

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

WELLKNOWN_KEYBASE = os.getenv('WELLKNOWN_KEYBASE')


def before_breadcrumb(crumb, hint):
    if crumb.get('category', None) == 'django.security.DisallowedHost':
        return None
    return crumb


def before_send(event, hint):
    if event.get('logger', None) == 'django.security.DisallowedHost':
        return None
    return event


sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    before_breadcrumb=before_breadcrumb,
    before_send=before_send,
)
