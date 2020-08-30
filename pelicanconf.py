#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'David'
SITENAME = 'IT journey'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FAVICON = 'images/favicon.png'

THEME = 'pelican-themes/pelican-bootstrap3/'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['i18n_subsites']

MARKDOWN = {
    'extension_configs': {
        # Needed for code syntax highlighting
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # This is for enabling the TOC generation
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
    },
    'output_format': 'html5',
}
