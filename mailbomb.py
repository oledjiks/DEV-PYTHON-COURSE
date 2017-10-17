#!/usr/bin/env python
'''
testmailbomb.py
------------------------------------------------------

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


'''

import socket, smtplib, struct

def sendmess(fromaddrs, toaddrs, msg):
    server = smtplib.SMTP('localhost')
    server.sendmail(fromaddrs, toaddrs, msg)
    server.quit()

code = 777
host = 'localhost'
port = 8888
fromaddr = 'From: it@floratelecom.ru'
toaddr = 'To: oledjiks@bk.ru'
msgs = 'This is the end!)'

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
server.settimeout(15)
while 1:
    try:
        mess, addr = server.recvfrom(1024)
        mess = struct.unpack('!i', mess)[0]
        if mess == code:
            print('code ok... ', mess)
    except socket.timeout as err:
        print(err)
        sendmess(fromaddr, toaddr, msgs.encode('utf-8'))
        break
server.close()