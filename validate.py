#!/usr/bin/env python

import re

def inputMailAddress():
    while True:
        s = input('Введите адрес электронной почты: ')
        valid = re.match(r'[\w\d.\-]+@[\w\d.\-]+', s)
        if valid == None:
            print('Пожалуйста введите корректный e-mail ( name@organization.domain )')
            continue
        else:
            return s

def inputTelNumber():
    while True:
        s = input('Введите телефонный номер: ')
        valid = re.match(r'^[(]{1}[0-9]{3}[)]{1}[0-9]{5,10}$', s)
        if valid == None:
            print('Пожалуйста введите корректный номер телефона ( (code)number )')
            continue
        else:
            return s

def inputData():
    while True:
        s = input('Введите дату: ')
        valid = re.match(r'\d{4}-\d{2}-\d{2}', s)
        if valid == None:
            print('Пожалуйста введите корректную дату ( yyyy-mm-dd )')
            continue
        else:
            ss = s.split('-')
            ss = [int(x) for x in ss]
            if ss[0] >= 1 and 12 >= ss[1] >= 1 and 31 >= ss[2] >= 1:
                return s
            else:
                print("Год должен быть больше 1, месяц от 1 до 12 и день от 1 до 31")
                continue

if __name__ == "__main__":
    mail = inputMailAddress()
    print(mail)
    tel = inputTelNumber()
    print(tel)
    date = inputData()
    print(date)