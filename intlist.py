#!/usr/bin/env python
with open('intlist.txt', 'r') as f:
    lst = f.readline().split(',')
    print(' '.join(lst))
    print(' '.join(lst[::-1]))