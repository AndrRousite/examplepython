#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/8 17:12
from wsgiref.simple_server import make_server

from wsgi import application

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

httpd = make_server('127.0.0.1', 8000, application)
print('Serving HTTP on port 8000...')

# 开始监听HTTP请求:
httpd.serve_forever()
