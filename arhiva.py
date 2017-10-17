#!/usr/bin/env python
from os import path
lst = input('Введите пути архивируемых файлов через пробел: ').split()
pname = ''.join([path.basename(fname)[0] for fname in lst])
for n in lst:
    with open(n, 'r') as fout:
        with open(pname, 'a') as fin:
            for l in fout:
                fin.write(l)