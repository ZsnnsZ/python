#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 20:06:42 2016

@author: macbookair
"""

from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd
#import time

today = date.today()
print today
start = date(today.year-1, today.month, today.day)
print start
quotes = quotes_historical_yahoo_ochl('AXP',start,today)
fields = ['date','open','close','high','low','volume']
dlist = []
for i in range(0,len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    dlist.append(x)
quotesdf = pd.DataFrame(quotes,index = dlist,columns = fields)
quotesdf = quotesdf.drop(['date'],axis = 1)
#print quotesdf 

#import numpy as np
#import pandas as pd
#dates = pd.date_range('20150201',periods = 15)
#dates = pd.DataFrame(range(1,16), index = dates,columns = ['value'])
#print dates
#Output:
#            value
#2015-02-01      1
#2015-02-02      2
#2015-02-03      3
#2015-02-04      4
#2015-02-05      5
#2015-02-06      6
#2015-02-07      7
#2015-02-08      8
#2015-02-09      9
#2015-02-10     10
#2015-02-11     11
#2015-02-12     12
#2015-02-13     13
#2015-02-14     14
#2015-02-15     15

#listtemp = []
#for i in range(0,len(quotesdf)):
#    temp = time.strptime(str(quotesdf.index[i]),"%Y-%m-%d")
#    listtemp.append(temp.tm_mon)
#print listtemp
#tempdf = quotesdf.copy()
#tempdf['month'] = listtemp
#print tempdf['month'].value_counts()
#Output:
#8     23
#12    22
#10    22
#6     22
#3     22
#9     21
#5     21
#4     21
#11    20
#7     20
#2     20
#1     19

#pd.merge(df1,df2,on = 'pubic')
