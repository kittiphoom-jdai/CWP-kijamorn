#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + "Z" * (8 - len(text)))

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)