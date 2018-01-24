#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/24 14:30
import urllib.request


__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

res = urllib.request.urlopen(urllib.request.Request("http://www.baidu.com"))
print(res.read())
