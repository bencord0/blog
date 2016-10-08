from __future__ import print_function
import os
import sys

import dj_database_url

Truthy = ['True', 'true', '1', 'yes', 'y']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUR_DIR = os.path.abspath(os.curdir)

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    import random
    SECRET_KEY = ''.join([random.SystemRandom().choice(
        'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    ) for i in range(50)])

DEBUG = os.environ.get('DEBUG', 'True') in Truthy
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
PORT = int(os.environ.get('PORT', '8000'))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'gunicorn',

    'blog.core',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

WSGI_APPLICATION = 'blog.wsgi.application'
ROOT_URLCONF = 'blog.urls'
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(CUR_DIR, 'static'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(CUR_DIR, 'templates')],
        'OPTIONS': {
            'environment': 'blog.core.jinja2.environment',
        },
    },
]

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///{}/db.sqlite3'.format(BASE_DIR))
}

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
