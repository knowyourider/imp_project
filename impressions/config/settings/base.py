"""
Django settings for impressions project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# from unipath import Path
from pathlib import Path
import json
from django.core.exceptions import ImproperlyConfigured

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 3-tier approach Using Unipath per Two Scoops
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# JSON-based secrets module
with open(BASE_DIR / 'config' / 'settings' / 'secrets.json') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """ Get the secret variable or return explicit exception. """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

ALLOWED_HOSTS = ['dinotracksdiscovery.org', 'www.dinotracksdiscovery.org', 
    'dev.dinotracksdiscovery.org', 'impdev.deerfield-ma.org', '127.0.0.1']

# Application definition

INSTALLED_APPS = (
    # 'django.contrib.sites',
    'ancillary.apps.AncillaryConfig',
    'core.apps.CoreConfig',
    'map.apps.MapConfig',
    'special.apps.SpecialConfig',
    'stories.apps.StoriesConfig',
    'supporting.apps.SupportingConfig',
    'themes.apps.ThemesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'impdb',
        'USER': 'impdb_user',
        'PASSWORD': 'Orra$1821',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

# STATIC_ROOT = os.path.join( SITE_ROOT, '../static')

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "imp_static"

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / "local_static",
)

# Media files (content images)
MEDIA_ROOT = BASE_DIR.parent / "imp_media"
MEDIA_URL = '/media/'

# Project specific constants
# 2 for draft, 3 for review, 4 for public
STATUS_LEVEL = 3

# for publi vs. private versions of the site?
SITE_ID = 1
# for devel vs. produciton diffes: google analytics in base.html
IS_PRODUCTION = False

# For 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
