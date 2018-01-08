#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/8 17:15

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    content = '<h1>Hello, %s!</h1>' % (environ['PATH'][1:] or 'web')
    return [content.encode('utf-8')]
