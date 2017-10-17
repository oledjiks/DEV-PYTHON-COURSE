#!/usr/bin/env python

import os, fnmatch, sys, shutil


def locate(pattern, root):
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)


src = sys.argv[1]
reg = sys.argv[2]
dst = sys.argv[3]

for f in locate(reg, src):
    print(f)
    d = os.path.join(dst, os.path.basename(f))
    shutil.move(src, d)
