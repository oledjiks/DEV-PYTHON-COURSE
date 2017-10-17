#!/usr/bin/env python

import smtplib, random

def send_email(host, subject, to_addr, from_addr, body_text):

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject ,
        "",
        body_text
    ))

    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()

host = 'localhost'
mess = open('message.txt', 'r').read()
addrs = open('maillist.txt', 'r')
for a in addrs:
    t = a.strip('\n')
    f = 'output@mailserver.com'
    s = random.choice(('Best product', 'Happy fitness', 'New year sale!!', 'Development service',
                       'The biggest open-source software storage'))
    send_email(host, s, t, f, mess)
