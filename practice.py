# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:06:12 2018

@author: Dmob
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import turtle
import time
import random
import os
import dbm
import pickle
import copy
from collections import namedtuple
import re


class Time:
    """Represents the time of day.""" 
    #def print_time(time):
        #print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    def __add__(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def __lt__(self,other):
         a = self.hour, self.minute, self.second 
         b = other.hour, other.minute, other.second
         #if a>b: return True
         #if self.hour>other.hour: return True
         return a>b
    
time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 30   

time32 = Time()
time32.hour = 12
time32.minute = 3
time32.second = 3

print(time2.__lt__(time32))  
    #print_time(time2)

#Time.print_time(time2)
#time2.print_time()
###print(time2)


class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        #return '(%d,%d)' %(self.x,self.y)
        return '{},{}'.format(self.x,self.y)
    def __add__(self, other):
        if isinstance(other, Point):
            return self.x + other.x, self.y + other.y
        elif isinstance (other, tuple):
            return self.x +other[0],self.y + other[1]
    
    def __radd__(self,other):
        return self.__add__(other)
        
k = Point(3,5)
e = Point(3,5)

print(k+(4,7))
print(k+e)

print(type(k+e))
print(type(k+(4,7)))

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))