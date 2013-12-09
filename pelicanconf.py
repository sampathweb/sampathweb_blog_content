#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = 'Ramesh Sampath'
SITENAME = 'Ramesh Sampath'
SITESUBTITLE = 'Thoughts and Experiments of an aspiring Data Scientist'
SITEURL = '' # change in publishconf.py

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Central'
DEFAULT_LANG = 'en'

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = os.path.join(os.environ.get('HOME'),
                     'code/blog/pelican-octopress-theme')
PLUGIN_PATH = os.path.join(os.environ.get('HOME'),
                           'code/blog/pelican-plugins')
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']


# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('Home Page', 'http://www.sampathweb.com'),
             ('About Me', '/about-me.html')]
NEWEST_FIRST_ARCHIVES = False

#Github include settings
GITHUB_USER = 'sampathweb'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
EXTRA_HEADER = open('_nb_header.html').read()

DEFAULT_PAGINATION = 10

# Sharing
TWITTER_USER = 'sampathweb'
GOOGLE_PLUS_USER = 'sampathweb'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 5
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Search
SEARCH_BOX = True

GOOGLE_ANALYTICS = 'UA-35953508-1'
DISQUS_SITENAME = 'sampathweb'

# STATIC_OUT_DIR requires https://github.com/jakevdp/pelican/tree/specify-static
#STATIC_OUT_DIR = ''
#STATIC_PATHS = ['images', 'figures', 'downloads']
#FILES_TO_COPY = [('favicon.png', 'favicon.png')]

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

