#! -*- coding:utf-8 -*-

"""
@author:Conner
@version:1.0
@date:13-8-19
@description:网盟shopping模块业务逻辑层，处理请求业务逻辑
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from googleler.config import settings
from googleler.views.base import BaseHandler
from googleler.lib.util.logger_util import logger


class IndexHandler(BaseHandler):
    """
    首页

    """

    def get(self):
        try:
            self._event('index')
            self.render(settings.index_template)
        except Exception as e:
            logger.error('[message: %s]' % e.message)


class ArticleHandler(BaseHandler):
    """
    首页

    """

    def get(self):
        try:
            self._event('index')
            self.render(settings.detail_template)
        except Exception as e:
            logger.error('[message: %s]' % e.message)