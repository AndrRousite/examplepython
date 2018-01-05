#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/5 13:46
import hashlib
import hmac
import json
from _datetime import datetime
import os
import re
import threading

import time

import itertools
from functools import reduce
from urllib import request

import psutil as psutil
from pip._vendor import requests
from pip._vendor.requests.packages import chardet

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

#  only works on Unix/Linux/Mac system
if os.name != 'nt':
    print('Process (%s) start ...' % os.getpid())
    pid = os.fork()

    if pid == 0:
        print('I\'m child process (%s) and my parent is %s ' % (os.getpid(), os.getppid()))
    else:
        print('I\'m (%s) just created a child process (%s) ' % (os.getpid(), pid))


# 新线程执行的代码:
def loop():
    # print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 0:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    # print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

print(re.split(r'\s+', 'a   b c '.strip(' ')))


def is_valid_email(email):
    if re.match('.+@.+\.com', email):
        return True
    else:
        return False
    pass


print(is_valid_email('someone@gmail.com'))

print('%d' % datetime.now().timestamp())

md5 = hashlib.md5()

md5.update('123456'.encode('utf-8'))

print(md5.hexdigest())

key = b'liu-feng'

message = b'123456'

h = hmac.new(key, message, digestmod='MD5')

print(h.hexdigest())

natuals = itertools.chain('ABC', 'DEF')

for n in natuals:
    print(n)


def qiuhe(n):
    nt = itertools.takewhile(lambda x: x <= 2 * n, itertools.count(1, 2))
    ns = []
    k = 1
    for i in nt:
        ns.append(4 * k / i)
        k = -k
    num = reduce((lambda x, y: x + y), ns)
    return num


print(qiuhe(100))

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print("Status:", f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' % (k, v))
#     d = json.loads(data.decode('utf-8'))
#     for p, s in d.items():
#         print('%s:%s' % (p, s))

# r = requests.get('https://www.douban.com/')
# print(r.text)


d = chardet.detect(b'hello world !')

print(d)

data = '哈哈'.encode('gbk')
print(type(data))
d = chardet.detect(data)

print(d)

s = data.decode('gbk')
print(type(s))
print(s)

print(psutil.cpu_times())

print(psutil.version_info)
print(psutil.virtual_memory())
print(psutil.swap_memory())

print(psutil.pids())
