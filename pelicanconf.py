# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = 'Bruno Masoller'
SITENAME = 'Descubriendo el mundo tecnológico'
SITEURL = ''  # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extras', 'images', 'pdfs', 'others']
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/manifest.json': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify', 'ipynb.markup', 'pelican_javascript', 'render_math']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

DEFAULT_METADATA = {
    'status': 'draft',
}

# General Settings --------------------------------------------------------------

SITESUBTITLE = 'Blog orientado a la discusión de tecnologías'
SITEIMAGE = '/images/profile.jpg width=250 height=250'
DESCRIPTION = 'Descubriendo el mundo tecnológico es un blog de discusión sobre muchas tecnologías y algunas no tanto XD'

DISPLAY_PAGES_ON_MENU = False

SOCIAL = (
	('github', 'https://github.com/brunomaso1'),
	('linkedin', 'https://www.linkedin.com/in/brunomaso1'),
	('twitter', 'https://twitter.com/brunomaso11'),
)

GITHUB_URL = 'https://github.com/brunomaso1'
TWITTER_USERNAME = '@brunomaso11'

HIDE_AUTHORS = True

# Tabla de contenido:
MARKDOWN = {
	'extension_configs': {
		'markdown.extensions.toc': {
		  'title': 'Tabla de contenido:',
		},
		'markdown.extensions.codehilite': {'css_class': 'highlight'},
		'markdown.extensions.extra': {},
		'markdown.extensions.meta': {},
	},
	'output_format': 'html5',
}

SEARCH_BOX = True

# Theme settings --------------------------------------------------------------

THEME = 'themes/pelican-alchemy/alchemy'

LINKS = (
	('CRISP-DM', SITEURL + '/pages/crisp-dm.html'),
   ('Python.org', 'http://python.org/'),
   ('Jinja2', 'http://jinja.pocoo.org/'),
)



ICONS = [
    ('github', 'https://github.com/brunomaso1'),
	('linkedin', 'https://www.linkedin.com/in/brunomaso1'),
	('twitter', 'https://twitter.com/brunomaso11'),
]

PYGMENTS_STYLE = 'monokai'
RFG_FAVICONS = True

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

# Theme settings --------------------------------------------------------------

IPYNB_SKIP_CSS = False
IPYNB_FIX_CSS = True
IGNORE_FILES = ['.ipynb_checkpoints']