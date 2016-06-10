#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
import datetime

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
UTILITIES = os.path.join(PROJECT_ROOT, 'utilities')
sys.path.insert(1, UTILITIES)
import filters

LOAD_CONTENT_CACHE = False
AUTORELOAD = True
IGNORE_CACHE = True
AUTHOR = u'CyberGreen'
SITENAME = u'CyberGreen Statistics'
DEFAULT_LANG = u'en'
PATH = 'content'
STATIC_PATHS = ['extra/CNAME', 'data']
EXTRA_PATH_METADATA = {
  'extra/CNAME': {'path': 'CNAME'},
}
OUTPUT_PATH = 'output'
TIMEZONE = 'UTC'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
LINKS = (('', ''),)
SOCIAL = (('', ''),)
DEFAULT_PAGINATION = False
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
ARCHIVES_SAVE_AS = False
THEME = os.path.join(PROJECT_ROOT, 'theme')
THEME_STATIC_DIR = 'static'
THEME_STATIC_PATH = os.path.join(THEME, THEME_STATIC_DIR)
DISPLAY_DATE_FORMAT = '%Y-%m-%d'
DISPLAY_TIME_FORMAT = '%H:%M:%S'
DISPLAY_DATETIME_FORMAT = '{0}T{1}'.format(DISPLAY_DATE_FORMAT,
                                           DISPLAY_TIME_FORMAT)
TIMESTAMP = datetime.datetime.now().strftime(DISPLAY_DATE_FORMAT)
SUMMARY_MAX_LENGTH = 25
JINJA_EXTENSIONS = [
  'jinja2.ext.do',
  'jinja2.ext.with_',
  'jinja2.ext.loopcontrols'
]
JINJA_FILTERS = {
  'where': filters.where,
  'markdown': filters.markdown,
  'natsort': filters.natsort,
  'tojson': filters.tojson,
  'debug': filters.debug,
  'search': filters.search,
  'first_or_default': filters.first_or_default,
}
PLUGIN_PATHS = [os.path.join(PROJECT_ROOT, 'plugins')]
PLUGINS = [
  'datastore',
  'datastore_api',
  'datastore_assets',
  'pelican_alias'
]

# DATASTORE PLUGIN CONFIGURATION
DATASTORE = {
    'location': os.path.join(PROJECT_ROOT, 'content', 'data'),
    'formats': ['.csv'],
    'intrafield_delimiter': '~*',
    'true_strings': ['TRUE', 'True', 'true'],
    'false_strings': ['FALSE', 'False', 'false'],
    'none_strings': ['NULL', 'Null', 'null', 'NONE', 'None', 'none',
                     'NIL', 'Nil', 'nil', '-', 'NaN', 'N/A', 'n/a', ''],
    'api': { # settings for the datastore_api plugin
        'base': 'api', # directory relative to `output`
        'formats': ['json', 'csv'], # output API in these formats
        'filters': {
            # Key must match a datastore file name.
            # Values must match headers in that file.
            'entries': ['year'],
            'datasets': ['category']
            #'places': ['region']
        },
        'exclude': [] # datastore files to exclude from API (by name of type)
    },
    'assets': {
        'location': 'downloads'
    }
}

# CyberGreen configuration
CGR = {
    'scheme': u'',
    'domain': u'',
    'logo': u'/static/images/cybergreen-logo-beta.png',
    'logosquare': u'/static/images/cybergreen-logo-square.png',
    'survey': {
    },
    'sponsor': {
      'name': u'Cybergreen',
      'domain': u'https://www.cybergreen.net/',
    },
    'analytics': {
      'google': u''
    },
    'years': [u'2016',u'2015'],
    'current_year': u'2016',
    'previous_year': u'2015',
    'na': u'n/a', 
    'twitter': '',
    'author': {
        'name': AUTHOR,
    }
}

SITEURL = u'{0}{1}'.format(CGR['scheme'], CGR['domain'])
SITELOGO = CGR['logo']
# If `config_instance` exists, load it for instance-specific configuration.
# See `config_instance.example` to get started.
try:
  from config_instance import *
except ImportError:
  pass
