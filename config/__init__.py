#! -*- coding:utf-8 -*-

"""
@author:Conner
@version:1.0
@date:13-11-18
@description:导入配置信息到setting对象
"""
import os
from . import development, production
from googleler.lib.util.config_util import setting_from_object
from googleler.lib.util.dict2object import Dict2Obj

#加载环境变量
LOVER_ENV = os.environ.get('LOVER_ENV', 'development')

config = development

if LOVER_ENV.lower() in ["production"]:
    config = production

settings = Dict2Obj(setting_from_object(config))

del LOVER_ENV