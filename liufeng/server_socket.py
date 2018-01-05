#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/5 17:36
import socket
import threading

import time

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
s.bind(('127.0.0.1', 9090))

s.listen(5)

print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        print(type(list(addr)))
        print('%s:%s=====>' % addr, data.decode('utf-8'))
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(data)
    sock.close()
    print("Closed from %s:%s" % addr)
    pass


while True:
    # 接收一个新的连接
    sock, addr = s.accept()
    # 创建新的线程来处理连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
