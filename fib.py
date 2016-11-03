#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:07:44 2016

@author: macbookair
"""
from math import sqrt
import math
def hanoi(a,b,c,n):
    if n==1:
        print a,'->',c
    else:
        hanoi(a,c,b,n-1)
        print a,'->',c
        hanoi(b,a,c,n-1)
        
def fib(n):
    if n==0:
        return n
    if n==1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
        
def isprime(n):
    if n == 1:
        return False
    for j in range(2,int(sqrt(n))+1):
        if n%j == 0:
            return False
    return True
    
def ismolisen(n):
    if isprime(n):
        m = 2**n - 1
        if isprime(m):
            return True
        else:
            return False
    else:
        return False

def outmolisen():
    a = 1
    c = 0
    while 1:
        if ismolisen(a):
            b = 2**a - 1
            print(b)
            c+=1
        a+=1
        if c == 6:
            break
            
#hanoi('a','b','c',4)
#==============================================================================
# for i in range(10):
#     print fib(i)
#==============================================================================
#outmolisen()
#if None:
#    print 1
#else:
#    print 0
def test(x):
    if isinstance(x, list):
        x.append(4)
        print x
    elif isinstance(x, int):
        x += 1
        print x
        
def my_power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s
    
#print my_power(-3)
#print my_power(3,3)
#9
#27

#def f(x):
#     a = 7
#     print a + x
#a = 5
#f(3)
#print  a
#
#10
#5 


    