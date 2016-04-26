# -*- coding: utf-8 -*-

from configurations import Configuration
import os

import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('stoqs')

env = environ.Env()


class Common(Configuration):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = env("DJANGO_SECRET_KEY", default='PLEASE_CHANGE_ME')

    # SECURITY WARNING: don't run with debug turned on in production!

    DEBUG = env.bool("DJANGO_DEBUG", True)

    ALLOWED_HOSTS = []

    DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    )

    THIRD_PARTY_APPS = (
        'multigtfs',
    )

    LOCAL_APPS = (
        'allbus.thebus',
    )

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'config.urls'

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
    ]

    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
    # http://django-configurations.readthedocs.org/en/latest/values/#configurations.values.DatabaseURLValue

    DATABASES = {
        'default': env.db("DJANGO_DATABASE_URL",
                          default="postgis://allbus:allbus@localhost/allbus"),
    }

    # Internationalization
    # https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

    STATIC_URL = '/static/'

    GEOS_LIBRARY_PATH = env("DJANGO_GEOS_LIBRARY_PATH", default='')
    GDAL_LIBRARY_PATH = env("DJANGO_GDAL_LIBRARY_PATH", default='')
    POSTGIS_VERSION = env("DJANGO_POSTGIS_VERSION", default=('',))

    THEBUS_API_CLIENT_TOKEN = env('THEBUS_API_CLIENT_TOKEN', default=None)
