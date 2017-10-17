#!/usr/bin/env python

from math import factorial as fact

def combination(L, n):
    result = []
    try:
        for i in L:
            result.append(fact(int(n)) / (fact(int(i)) * fact(int(n) - int(i))))
    except ValueError as err:
        print(err)
    return result

def placing(L, n):
    result = []
    try:
        for i in L:
            result.append(fact(int(n)) / fact((int(n) - int(i))))
    except ValueError as err:
        print(err)
    return result

def permutation(L):
    try:
        result = []
        for i in L:
            result.append(fact(int(i)))
    except ValueError as err:
        print(err)
    return result


