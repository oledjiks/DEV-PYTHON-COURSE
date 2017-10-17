#!/usr/bin/env python
from os import path
# первая часть считывания и добавления хоста в файл
names = {}
with open(path.normpath(r'C:\Users\Олег\Dropbox\DEV-PYTHON\resnames.txt'), 'r') as f:
	for i in f:
		a, n = i.rstrip('\n').split()
		names[a] = n
	print(names)
	a = input('Введите адрес и имя: ').strip(
	f.write(a)

''' вторая чаcть поиск в файле
with open('resnames.txt', 'r') as f:
    i = input('Введите имя или IP адрес для поиска (0 для выхода): ').strip()
	for l in f.readline():
        lst = l.split()
		if i in lst:
           print(lst)
        else:
			f.seek(0)
    	    continue
'''