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



def check_fermat(a,b,c,n):
    if n > int(2) and (a**n + b**n == c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn’t work.")   

def q():
    a1 = np.random.randint(-10,10)
    b1 = np.random.randint(astype(int))
    c1 = np.random.random_integers
    n1 = np.random.randint
    a=a1
    b=b1
    c=c1
    n=n1
    #return check_fermat(a, b, c, n)
    print (type(a1))
    print (type(b))
    print (type(c))
    print (type(n))
    

q()

#check_fermat(124,7,89,2) 