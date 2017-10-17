#!/usr/bin/env python

import hmac, sys, base64

if sys.argv[1] == '-c':
    password = input('Введите пароль для проверки подписи файла: ').encode('utf-8')
    hm = hmac.new(password)
    with open(sys.argv[2], 'rb+') as f:
        ff = f.readlines()
        h = base64.b64decode(ff.pop(-1))
        for line in ff:
            hm.update(line)
        if hm.hexdigest() == h:
            print('Файл корректен')
        else:
            print('Файл некорректен')
else:
    password = input('Введите пароль для подписи файла: ').encode('utf-8')
    hm = hmac.new(password)
    with open(sys.argv[1], 'rb+') as f:
        for line in f:
            hm.update(line)
    with open(sys.argv[1], 'a') as f:
        h = base64.b64encode(hm.digest())
        f.write('\n')
        f.write(h.decode('utf-8'))