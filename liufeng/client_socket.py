#!/usr/bin/python3

# @author liu-feng
# @email w710989327@foxmail.com
# @time 2018/1/5 17:46
import socket

__author__ = 'liu-feng'
__email__ = 'w710989327@foxmail.com'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9090))

print(s.recv(1024).decode('utf-8'))

while True:
    send = input()
    s.send(send.encode('utf-8'))
    recv = s.recv(1024).decode('utf-8')
    print('服务端答复：', recv)
    if not send or send == 'exit' or recv == 'exit':
        break
s.close()
