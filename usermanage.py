#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:00:38 2016

@author: macbookair
"""

#class userinfo():
#    user = {'name':'admin','pwd':123456}
users = {'admin':'123456'}
def newusers(users):
    name = raw_input("please enter your name:")
    while name in users.keys():
        name = raw_input("enter again:")
    else:
        pwd = raw_input("please enter the pwd:")
        users[name] = pwd

def oldusers(users):
    name = raw_input("please enter your name:")
    pwd = raw_input("please enter the pwd:")
    if name in users.keys() and pwd == users[name]:
        print name,'welcome back'
    else:
        print 'login incorrect'
        
def login():
    option = '''
            (N)ew User Login 
            (O)ld User Login
            (E)xit 
            '''
    option = raw_input(option)
    if option == 'N':
        newusers(users)
    elif option == 'O':
        oldusers(users)
    elif option == 'E':
        exit
        
if __name__ == '__main__':
    login()
        