#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jim'
SITENAME = u'Robot & ME'
SITEURL = u'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = u'Blogger'
SITEDESCRIPTION = u'%s\ and Robot whisper' % AUTHOR
SITELOGO = u'../theme/img/profile.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

ROBOTS = u'index, follow'

THEME = u'/Users/jingqiu/Projects/robotame/env/lib/python2.7/site-packages/pelican/themes/flex'
PATH = 'content'
TIMEZONE = 'Asia/Hong_Kong'
DEFAULT_LANG = u'cn'
OG_LOCALE = u'en_US'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

# Blogroll
LINKS = (('Portfolio', 'http://www.lifelongblog.cn/'),)

# Social widget
SOCIAL = (('linkedin', 'https://cn.linkedin.com/in/jingqiu'),
          ('github', 'https://github.com/kingqiu'),
	  ('google', 'http://www.baidu.com'),)

MEMUITEMS = (('Archives', '/archives.html'),
	     ('Categories','/categories.html'),)

CC_LICENSE = {
	'name': 'Creative Commons Attribution-ShareAlike',
	'version': '4.0',
	'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2015

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
