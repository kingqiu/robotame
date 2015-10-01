#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jim'
SITENAME = u'Robot & ME'
SITEURL = u'http://localhost:8000'
SITETITLE = u'Robot & ME'
SITESUBTITLE = u'Jim & I whisper here...'
SITEDESCRIPTION = u'We whisper here...'
SITELOGO = u'../theme/img/profile.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

ROBOTS = u'index, follow'

THEME = u'/Users/jingqiu/Projects/robotame/env/lib/python2.7/site-packages/pelican/themes/flex'
PATH = 'content'
TIMEZONE = 'Asia/Hong_Kong'
DEFAULT_LANG = u'cn'
OG_LOCALE = u'en_US'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True


MAIN_MENU = True

# Blogroll
LINKS = (('my profile', 'http://www.lifelongblog.cn/'),)

# Social widget
SOCIAL = (('linkedin', 'https://cn.linkedin.com/in/jingqiu'),
          ('github', 'https://github.com/kingqiu'),
	  ('twitter', 'https://twitter.com/jingqiu'),
	  ('facebook','https://www.facebook.com/jingqiu'),)

#DISPLAY_CATEGORISE_ON_MENU = True
#DISPLAY_PAGES_ON_MENU = True

MEMUITEMS = (('Archives', '/archives.html'),)

CC_LICENSE = {
	'name': 'Creative Commons Attribution-ShareAlike',
	'version': '4.0',
	'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2015

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
