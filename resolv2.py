#!/usr/bin/env python

f = open(r"D:\resnames.txt", 'r')
i = None
while i != '0':
	i = input('Введите имя или IP адрес для поиска (0 для выхода): ').strip()
	for l in f.readlines():
		lst = l.split()
		if i in lst:
			print(lst)
		else:
			f.seek(0)
			continue
f.close()