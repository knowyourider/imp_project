"""
Production Django settings for impression project.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Project specific constants
# 2 for draft, 3 for review, 4 for public
STATUS_LEVEL = 4

# for publi vs. private versions of the site?
SITE_ID = 1

SECURE_SSL_REDIRECT = True
# for devel vs. produciton diffes: google analytics in base.html
IS_PRODUCTION = True
