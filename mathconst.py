#!/usr/bin/env python
import math
mathc = {'pi': math.pi, 'e': math.e, 'inf': math.inf}
i = input('Введите констану(pi,e,i) и точность через двоеточие > ').split(':')
c, t = i
if c in mathc.keys():
    d = '%.' + t + 'f'
    print(d % mathc[c])
else:
    print('Нет такой константы')