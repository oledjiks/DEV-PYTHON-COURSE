#!/usr/bin/env python

'''
Пример файла конфига listmon:
http://yandex.ru
http://cvetopttorg.spb.ru
http://mail.ru
'''

import requests, datetime, time, smtplib

fromaddr = 'From: it@floratelecom.ru' # адрес отправителя
toaddr = 'To: oledjiks@bk.ru'       # адрес получатея

def sendmess(fromaddr, toaddrs, msg):
    server = smtplib.SMTP('localhost')
#    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

with open('listmon', 'r') as f:
    try:
        while True:
            for url in f:
                url = url.strip('\n')
                try:
                    r = requests.get(url)
                    if r.status_code != 200:
                        print('{} - cервис недоступен, код ошибки: {}'.format(datetime.datetime.now(), r.status_code))
                    else:
                        print('{} - сервис: {} - OK'.format(datetime.datetime.now(), url))
                except requests.ConnectionError as err:
                    msg = '{} - невозможно подлкючиться к {}'.format(datetime.datetime.now(), url)
                    print(msg)
                    sendmess(fromaddr, toaddr, msg.encode('utf-8'))
            f.seek(0)
            print('--------------------------------------------')
            time.sleep(10)
    except KeyboardInterrupt as err:
        print(err)