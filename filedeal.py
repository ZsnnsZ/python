#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:08:57 2016

@author: macbookair
"""

#w和w+都会清空原文件内容，a和a＋只能追加
#r读，w写，a追加
#r＋＝r＋w
#w＋＝w＋r
#a＋＝a＋r
#
#二进制
#rb，wb，ab，rb＋，wb＋，ab＋

#序列（元组，列表，字符串）
#（1）序列类型函数
#
#enumerate(), reversed(), sorted(), zip()
#list = ['a','b','c']
#estr = 'cds'
#for i,j in enumerate(estr):
#    print i+1,j
#for i in reversed(list):
#    print i
#print sorted(list)
#alist = ['cd','ac','ab','ca','bd']
#
#alist.sort()
#alist.reverse()
#print alist
#blist = [1,2,3]
#for x in zip(alist,blist,list):
#    print x
#（2）字符串类型方法
#
#join(), strip(), replace(), split(), translate(),startswith()
#
#其中translate()需要使用maketrans()方法：
##astr = 'hello'
#
#print 'a'.join(astr)
#print astr.replace('e','a')
##str.strip([chars]),移除字符串头尾指定的chars
#print astr.strip('h')
#print astr
#
#print astr.split('l')
#print astr
#
#print astr.startswith()
#from string import maketrans   # 引用 maketrans 函数。
#
#intab = "aeiou"
#outtab = "12345"
#trantab = maketrans(intab, outtab)
#
#str = "this is string example....wow!!!"
#print str.translate(trantab)
#（3）列表类型方法
#
#append(), count(), extend(), insert(), pop(), sort()

    
#def func(args1,*argst):
#    print args1
#    print argst
#    
#func('b','b','c','a')
#

#keys = ['a','b','c']
#values = [1,2,3]
#aDict = dict(zip(keys,values))
#print aDict
#
#print aDict.get('f')
#
#bDict = {'d':4}
#
#aDict.update(bDict)
#print aDict

#my_list = [s.lower() for s in 'Life is short, you need Python.'.split(' ')]
#print 'short' in my_list

a = {1,2,3,4}
b = {2,3,5,6}
a.union(b) == a|b
