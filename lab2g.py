#!/usr/bin/env python3
'''
Author: Alina Gansen
Author ID: agansen 141407239
Date: 2026/05/19
'''
import sys

if len(sys.argv) == 1:
    timer = 3
    while timer > 0:
        print(timer)
        timer -= 1
    print("blast off!")
else:
    timer = int(sys.argv[1])
    while timer > 0:
        print(timer)
        timer -= 1
    print("blast off!")
