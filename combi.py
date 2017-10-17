#!/usr/bin/env python
from math import factorial as fact

try:
    n, m = tuple(input('Введите параметры последовательности через пробел: ').split())
    r = fact(int(n)) / fact((int(n) - int(m)))
    p = fact(int(n))
    c = fact(int(n)) / (fact(int(m)) * fact(int(n) - int(m)))
    print('Количество размещений: ', r)
    print('Количество перестановок: ', p)
    print('Количество сочетаний: ', c)
except ValueError:
    print('Не подходящее значение последовательности')
