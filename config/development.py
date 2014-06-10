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
DEBUG = True
OFFLINE = False
PRODUCTION = False

#LOG
LOG_PATH = 'D:/xincloud/task_list/task_mmo/log/'
FILE_PATH = 'D:/xincloud/task_list/task_mmo/pic/'
LOG_FILE = 'development.log'
DEFAULT_LOG_SIZE = 1024*1024*50

# MEMCACHED
MEMCACHED = {
    'default': ('127.0.0.1:11211', ),
}
INDEX_TIMEOUT = 60 * 60 * 24
SEARCH_TIMEOUT = 60 * 60 * 24
SEARCH_NEW_HOT_TIMEOUT = 60 * 3
