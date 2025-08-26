"""
Local Django settings for impression project.
"""

from .base import *

DEBUG = True

# For local development
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Optional: More verbose logging for development
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Project specific constants
# 2 for draft, 3 for review, 4 for public
STATUS_LEVEL = 2

# for publi vs. private versions of the site?
# SITE_ID = 1
