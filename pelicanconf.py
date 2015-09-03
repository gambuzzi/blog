#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roberto Gambuzzi'
SITENAME = u"Frammenti di codice"
SITESUBTITLE = u"e amenità varie"

SITEURL = 'http://blog.gambuzzi.it'

PATH = 'content'
CACHE_PATH = '/tmp/pelicancache1'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
         ('Python.org', 'http://python.org/'),
         ('Martin Fowler', 'http://martinfowler.com/'),
         ('Joel On Software', 'http://www.joelonsoftware.com/'),
         ('Alan Storm', 'http://alanstorm.com/'),
        )
# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/gbinside'),
          ('GitHub', 'https://github.com/gbinside'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme/mytheme"

DISQUS_SITENAME = 'bloggambuzzi'

GOOGLE_ANALYTICS = 'UA-54060223-1'

GAUGES = '550ab326de2e26670a017635'

#GITHUB_URL = 'http://github.com/gbinside/'

TWITTER_USERNAME = 'gbinside'

DEFAULT_DATE_FORMAT = '%d %m %Y'

DIRECT_TEMPLATES = (('tags', 'categories', 'authors', 'archives', 'search', 'test'))

STATIC_PATHS = [ 'images', 'extras', ]

EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/drafts.htaccess': {'path': 'drafts/.htaccess'},
    }

#JINJA_EXTENSIONS = ['jinja2.ext.i18n']
#I18N_GETTEXT_LOCALEDIR = 'theme/mytheme/translations/'
#I18N_GETTEXT_DOMAIN = 'messages'

PLUGIN_PATHS = ["plugins"]

PLUGINS = [
    #'subcategory',
    'sitemap',
    'i18n_subsites',
    'simpletranslate',
    'morevars',
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

I18N_SUBSITES = {
    'en': {
        'SITENAME': u'Code\'s Fragment',
        'SITESUBTITLE': u"and various amenities",
    },
}
