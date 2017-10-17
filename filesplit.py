#!/usr/bin/env python
try:
    with open('fileforsplit.txt', 'r') as f:
        for s in f:
            fname = s.rstrip('\n').split()[0] + '.txt'
            with open(fname, 'w') as f1:
                f1.write(s)
except Exception as e:
    print(e)
