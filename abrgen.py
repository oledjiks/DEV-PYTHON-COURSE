#!/usr/bin/env python
import random

abr = {'A': ['Abstract', 'Application', 'Apple'],
       'B': ['Basic', 'Base', 'Binary'],
       'C': ['Connect', 'City', 'College'],
       'P': ['Pretty', 'Pig', 'Protocol']}
a = None
while a != '0':
    a = input('Введите аббревиатуру (0 для выхода): ').upper()
    print(' '.join([random.choice(abr.get(i, '*')) for i in a]))