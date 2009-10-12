_ = lambda s:s

import os.path

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.split(PROJECT_ROOT)[-1]



# DEBUGGING

DEBUG = False
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ()



# CACHE

CACHE_BACKEND = 'locmem://'
CACHE_MIDDLEWARE_KEY_PREFIX = '%s_' % PROJECT_NAME
CACHE_MIDDLEWARE_SECONDS = 600



# EMAIL / ERROR NOTIFY

SERVER_EMAIL = 'pb@philippbosch.de'

ADMINS = (
    ('Philipp Bosch', 'philipp.bosch@me.com'),
)

MANAGERS = ADMINS



# DATABASE

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = PROJECT_NAME
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''



# I18N

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de'
LANGUAGES = (
    ('de', 'Deutsch'),
)
USE_I18N = False

from django.utils.translation import ugettext_lazy as _



# URLS

SITE_ID = 1

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

ROOT_URLCONF = '%s.urls' % PROJECT_NAME



# APPLICATION / MIDDLEWARE

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.markup',
    
    'south',
    
    'attendance',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)



# SECRET

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)



FORCE_SCRIPT_NAME = ''



# SOUTH

SOUTH_AUTO_FREEZE_APP = True



# AUTH

LOGIN_REDIRECT_URL = '/'


try:
    execfile(os.path.join(os.path.dirname(__file__), "settings_local.py"))
except IOError:
    pass

