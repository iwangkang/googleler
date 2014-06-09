#! -*- coding:utf-8 -*-

"""
@author:Conner
@version:1.0
@date:13-11-19
@description:默认配置信息
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from googleler.config.base import *

# BASE
DEBUG = False
OFFLINE = False
PRODUCTION = True

#LOG
LOG_PATH = '/home/wangkang/log/bootstrap'
FILE_PATH = '/home/wangkang/srv/LOVER_BOSEIDON/bootstrap/static/image/meinv/'
LOG_FILE = 'product.log'
DEFAULT_LOG_SIZE = 1024*1024*50

# MEMCACHED
MEMCACHED = {
    'default': ('127.0.0.1:11211', ),
}
INDEX_TIMEOUT = 60 * 9
SEARCH_TIMEOUT = 60 * 60 * 24
SEARCH_NEW_HOT_TIMEOUT = 60 * 3