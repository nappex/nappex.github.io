#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'David'
SITENAME = 'Sailing the IT sea'
SITEURL = ''
LANDING_PAGE_TITLE = "Welcome to " + SITENAME

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

FAVICON = 'images/favicon.png'
THEME = 'pelican-themes/elegant'
TYPOGRIFY = True

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images',
                f'theme/images',
                'extra/robots.txt']

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = [
    "extract_toc",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
]



SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"

# METADATA
# status can be 'draft', 'hidden', 'published'
DEFAULT_METADATA = {
    'status': 'published',
}

# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': '/robots.txt'}
# }

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

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.meta': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
        'markdown.extensions.toc': {
            'permalink': 'true',
        },
    },
    'output_format': 'html5',
}

# Landing Page
PROJECTS_TITLE = "Related Projects"
PROJECTS = [
    {
        "name": "Invoice generator",
        "url": "https://github.com/nappex/invoice_generator",
        "description": "Simple invoice generatot in python",
    },
    {
        "name": "Freezeyt (NOT MINE PROJECT)",
        "url": "https://github.com/encukou/freezeyt",
        "description": "Static web site generator created by czech community of PyLadies",
    },

]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
