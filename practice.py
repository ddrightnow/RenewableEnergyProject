# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:06:12 2018

@author: Dmob
"""

def a():
    print('+', '-'*4,end=' ')
    print('+', '-'*4,end=' ')
    print('+')



def b():
    print ('|','',' ',' ','|','',' ',' ','|')
    print ('|','',' ',' ','|','',' ',' ','|')
    print ('|','',' ',' ','|','',' ',' ','|')
    print ('|','',' ',' ','|','',' ',' ','|')

def c():
    return a(),b(),a(),b(),a()
    


c()