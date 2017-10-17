#!/usr/bin/env python

name = input('Введите полный путь файла: ')
with open(name, 'r') as f:
    for line in f:
    	