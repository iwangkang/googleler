#! -*- coding:utf-8 -*-
__author__ = 'niutong'

#!/usr/bin/env python

import multiprocessing

#bind = '0.0.0.0:8000'
bind = 'unix:/tmp/guge_gunicorn.sock'
workers = multiprocessing.cpu_count() * 2 + 1
#worker_class = 'egg:gunicorn#gevent'

user = 'root'

loglevel = 'warning'

#secure_scheme_headers = {
#    'X-SCHEME': 'https',
#    'X-FORWARDED-PROTOCOL': 'ssl',
#    'X-FORWARDED-PROTO': 'https',
#    'X-FORWARDED-SSL': 'on',
#}
#x_forwarded_for_header = 'X-FORWARDED-FOR'