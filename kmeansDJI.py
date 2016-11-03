#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 16:28:50 2016

@author: macbookair

聚类分析Python for Data Analysis
"""

#from numpy import vstack
#import numpy

from numpy import vstack
from scipy.cluster.vq import kmeans,vq
list1=[88.0,64.0,96.0,85.0]
list2=[92.0,99.0,95.0,94.0]
list3=[91.0,87.0,99.0,95.0]
list4=[78.0,99.0,97.0,81.0]
list5=[88.0,78.0,98.0,84.0]
list6=[100.0,95.0,100.0,92.0]
data = vstack((list1,list2,list3,list4,list5,list6))
centroids,_ = kmeans(data,2)
result,_= vq(data,centroids)
print result

#from scipy.cluster.vq import kmeans,vq
#from matplotlib.finance import quotes_historical_yahoo_ochl
#from datetime import datetime
#start = datetime(2014,7,1)
#end = datetime(2014,9,30)
#listDji = ['AXP','BA','CAT','CSCO','CVX','DD','DIS','GE','GS','HD','IBM',
#'INTC','JNJ','JPM','KO','MCD','MMM','MRK','MSFT','NKE','PFE','PG','T','TRV',
#'UNH','UTX','V','VZ','WMT','XOM']
#quotes = [ [0 for col in range(90)] for row in range(30)]
#listTemp = [ [0 for col in range(90)] for row in range(30)]
#for i in range(30):
#    quotes[i] = quotes_historical_yahoo_ochl(listDji[i], start, end)
#days = len(quotes[0])
#for i in range(30):
#    for j in range(days-1):
#        if (quotes[i][j][2] and quotes[i][j+1][2] and (quotes[i][j+1][2] >= quotes[i][j][2])):
#            listTemp[i][j] = 1.0   
#        else:
#            listTemp[i][j] = -1.0
#data = vstack(listTemp)
#centroids,_ = kmeans(data,4)   #float or double is supported
#result,_= vq(data,centroids)
#print result