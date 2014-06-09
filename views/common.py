#! -*- coding:utf-8 -*-

"""
@author:Conner
@version:1.0
@date:14-6-4
@description:
"""

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from tornado.web import utf8
from tornado.escape import json_encode
from googleler.config import settings
from googleler.views.base import BaseHandler
from googleler.lib.util.logger_util import logger
from googleler.lib.util.file_util import FileUtil


# class WaterfallHandler(BaseHandler):
#     """
#     跨域处理逻辑
#
#     """
#     CALLBACK = 'callback' # define callback argument name
#
#     def get(self):
#         try:
#             # begin_index = random.randint(0, 10000)
#             # end_index = begin_index + 20
#             # image_name_list = FileUtil.get_filename_list(settings.file_path, begin_index, end_index)
#             image_name_list = FileUtil.get_filename_list(settings.file_path, 0, 20)
#             image_list = list()
#             index = 1
#             for image_name in image_name_list:
#                 image = dict()
#                 image['imgid'] = index
#                 image['url'] = '/static/image/meinv/' + image_name
#                 im = Image.open(settings.file_path + image_name)
#                 image['height'] = im.size[1]
#                 image['width'] = im.size[0]
#                 image_list.append(image)
#                 index += 1
#             self.write(json_encode(image_list))
#         except Exception as e:
#             logger.error('[message: %s]; [host: %s]; [ip: %s]; [params: %s]' % (
#                 e.message, self.request.host, self.request.remote_ip, self.params.__str__()))
#
#     def finish(self, chunk=None):
#         """Finishes this response, ending the HTTP request."""
#         assert not self._finished
#         if chunk:
#             self.write(chunk)
#
#         # get client callback method
#         callback = utf8(self.get_argument(self.CALLBACK))
#         # format output with jsonp
#         self._write_buffer.insert(0, callback + '(')
#         self._write_buffer.append(')')
#
#         # call base class finish method
#         super(WaterfallHandler, self).finish() # chunk must be None