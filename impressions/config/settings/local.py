"""
Local Django settings for impression project.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition
# only adds mod_wsgi.server
# may not use wsgi express -- don't know how to use it with multiple settings files
#INSTALLED_APPS += ('mod_wsgi.server', )

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'impdb',
        'USER': 'impdb_user',
        'PASSWORD': 'dino$prints',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Project specific constants
# 2 for draft, 3 for review, 4 for public
STATUS_LEVEL = 2

# for publi vs. private versions of the site?
# SITE_ID = 1
