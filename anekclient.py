#!/usr/bin/env python

import socket

host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))