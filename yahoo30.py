#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:04:55 2016

@author: macbookair
"""

import urllib2
import re
dStr = urllib2.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
#getdStr=dStr.decode() 
#在python 3中urllib.read()返回bytes对象而非str，语句功能是将dStr转换成str,<nobr><small>(.*?)</small></nobr>
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?<small>(.*?)</small>.*?</tr>', dStr)
if m:
    for x in m:
        print x
    print '\n'
    print len(m)
else:  
    print 'not match'