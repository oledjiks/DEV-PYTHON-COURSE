#!/usr/bin/env python

import socket, struct

host = 'localhost'
port = 44444
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = struct.pack('!q', 352342352352345)
client.sendto(msg, (host, port))
d = client.recvfrom(1024)
reply = struct.unpack('!q', d[0])
print('Server reply: {}'.format(reply))
client.close()