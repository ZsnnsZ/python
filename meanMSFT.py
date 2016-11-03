#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:19:04 2016

@author: macbookair
"""

from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd

end = date.today()
start = date(end.year - 1, end.month, end.day)
quotesMS = quotes_historical_yahoo_ochl('MSFT', start, end)
attributes = ['date','open','close','high','low','volume']
quotesMSdf = pd.DataFrame(quotesMS, columns = attributes)

alist = []
for i in range(0, len(quotesMSdf)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    alist.append(y)
quotesMSdf.index = alist

blist = []
for i in range(0,len(quotesMSdf)): 
    blist.append(int(quotesMSdf.index[i][3:5]))
quotesMSdf['month'] = blist
quotesMSdf = quotesMSdf.drop(['date'], axis = 1)
#print(quotesMSdf.groupby('month').mean().close)
#quotesMSdf['16/02/16':'16/03/15'][quotesMSdf.close>52]
#quotesMSdf['16/02/16':'16/03/15'].sort('close', ascending = 1)[:5]
#quotesMSdf.ix['16/02/16':'16/03/15',['open','close']]
#pd.concat([sorted[:5],sorted[int(len(sorted)-5):]])
#quotesMSdf[quotesMSdf.close > quotesMSdf.open]['month'].value_counts
from matplotlib import pyplot as plt
closeMeans = quotesMSdf.groupby('month').mean().close
listMSFT = []
for i in range(1,13):
    listMSFT.append(closeMeans[i])
listMSFTindex = closeMeans.index
plt.plot(listMSFTindex, listMSFT, linestyle = '-', color = 'red', linewidth = 3, label = 'line1')#折线图，plt.plot(listMSFTindex,listMSFT，‘o’)散点图，plt.bar()柱状图
plt.title('MSFT')
plt.xlabel('month')
plt.ylabel('volume')
#plt.plot(label = 'line')图例
plt.legend(loc = 'upperleft')
plt.show()