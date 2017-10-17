#!/usr/bin/env python

import socket, time, struct
host = 'localhost'
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, port))
code = struct.pack('!i', 777)
while 1:
    try:
        s.sendto(code, (host, port))
        time.sleep(5)
    except (KeyboardInterrupt, SystemExit) as err:
        print(err)
        s.shutdown(1)


