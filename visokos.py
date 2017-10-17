#!/usr/bin/env python

try:
	year = int(input('Введите год: '))
	if year % 4 or (year % 100 == 0 and year % 400):
		print('Год не високосный')
	else:
		print('Год високосный')
except ValueError as err:
	print('Не правильное значение, год целое число')
