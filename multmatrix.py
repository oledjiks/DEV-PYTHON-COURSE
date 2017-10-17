#!/usr/bin/env python
'''
matrix1 sample file
1 2 3 
5 6 7 
9 10 1

matrix2 sample file
2 33 4
1 22 5
2 3 4
'''
import numpy as nm


def mxread(mf):
    with open(mf, 'r') as f:
        matrix = []
        for s in f:
            matrix.append([int(i) for i in s.split()])
        return matrix


m1 = nm.array(mxread('matrix1'))
m2 = nm.array(mxread('matrix2'))
try:
    print(m1 * m2)
except ValueError as err:
    print('Матрицы должны быть одинаковой размерности')
