#!/usr/bin/env python
import random
words = []
p = input('Введите путь файла: ')
with open(p, 'r') as f:
	words = [words.extend(w) for w in line.split() for line in f]

#    for line in f:
#        for w in line.split():
#            words.append(w)
for w in words:
    print(random.choice(words))