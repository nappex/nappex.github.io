#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

AUTHOR = 'David'
SITENAME = "The Snail's journey"
SITEURL = 'https://nappex.github.io/myblog'
LANDING_PAGE_TITLE = "Welcome to " + SITENAME + \
                    " through the IT world !"
THEME = 'elegant'
# FAVICON = 'content/extra/favicon.ico'
# SITELOGO = 'content/extra/favicon.ico'
TYPOGRIFY = True
TIMEZONE = 'Europe/Prague'
DEFAULT_LANG = 'en'

# PATHS
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'theme/images', 'extra']
USE_SHORTCUT_ICONS=True

# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},
#     # 'extra/CNAME': {'path': 'CNAME'},
#     # 'extra/LICENSE': {'path': 'LICENSE'},
#     # 'extra/README': {'path': 'README'},
# }

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



DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]

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
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"

# METADATA
# status can be 'draft', 'hidden', 'published'
DEFAULT_METADATA = {
    'status': 'draft',
}

# A list of filenames that should be retained and not deleted from the output directory.
# One use case would be the preservation of version control data.
OUTPUT_RETENTION = [".git"]
OUTPUT_PATH = 'output/myblog/'

SUMMARY_MAX_LENGTH = 50
SUMMARY_END_SUFFIX = '…'

# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': '/robots.txt'}
# }

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
            ('GitHub', 'https://github.com/nappex'),
            ('gmail', 'mailto:d.stroch@gmail.com'),
            ('You can add links in your config file', '#'),
            ('Another social link', '#'),
        )

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
