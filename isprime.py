# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import sqrt
def isprime(x):
    if x == 1:
        return False
    for j in range(2,int(sqrt(x))):
        if x%j == 0:
            return False
    return True
    
for i in range(2,101):
    if isprime(i):
        print i
    