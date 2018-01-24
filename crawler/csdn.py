#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/24 14:39
import urllib.request

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

values = {'username': "w710989327@foxmail.com", 'password': 'w15879418606'}
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url, data=values)
response = urllib.request.urlopen(request)

print(response.read())
