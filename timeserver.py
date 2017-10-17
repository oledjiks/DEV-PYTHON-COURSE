#!/usr/bin/env python

import socket, struct, datetime

host = 'localhost'
port = 44444
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)
t = datetime.datetime(1900, 1, 1)
while True:
    d = server.recvfrom(1024)
    received = struct.unpack('!q', d[0])
    addr = d[1]
    print('Received data: ', received)
    print('From: ', addr)
    data = datetime.datetime.now()
    data = (data - t).total_seconds()
    msg = struct.pack('!q', int(data))
    server.sendto(msg, addr)
server.close()