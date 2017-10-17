#!/usr/bin/env python
import os
p = os.environ['PATH'].split(':')
for pth in p:
    for root, dir, files in os.walk(pth):
            for name in files:
                fullname = os.path.join(root, name)
                if os.access(fullname, os.X_OK):
                    print(fullname)

