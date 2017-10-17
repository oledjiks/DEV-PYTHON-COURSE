#!/usr/bin/env python
from math import factorial
dlist = []
with open('diglist.txt', 'r') as f:
	for l in f:
		dlist.extend(l.split())
for i in range(len(dlist)):
	dlist[i] = int(dlist[i])
summ = 0
for i in dlist:
	summ += i
print('Сумма = ', summ)
srednee = summ / (len(dlist))
print('Среднее арифметическое = ', srednee)
pro = 1
for i in dlist:
	pro *= i
print('Произведение = ', pro)
print('Факториалы = ', end='')
for i in dlist:
	print(factorial(i), end=' ')