#!/usr/bin/env python
f, nf = input('Введите путь копируемого файла и через пробел полный путь нового файла: ').split()
with open(f, 'r') as fout:
    with open(nf, 'w') as fin:
        for l in f:
            fin.write(l)
