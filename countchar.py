#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:22:42 2016

@author: macbookair
"""

def countchar(str):
    list1 = [0]*26
    for i in range(0,len(str)):
        if (str[i] >= 'a'and str[i] <='z'):  
            list1[ord(str[i])-97] += 1
    print list1
if __name__ == "__main__":
    str = "Hope is a good thing."
    str = str.lower()
    countchar(str)