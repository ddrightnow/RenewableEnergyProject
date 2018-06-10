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



def is_power(a,b):
    if(a%b != 0):
        return False
    elif(a/b == 1):
        return True
    else:
        return is_power(a/b,b)

print(is_power(81,9))

'''
    elif a % b !=0 or b!=a**(1/i):
        for i in range (5):
            if a % b !=0 and b!=a**(1/i):
                i=i+1
                return True
            else:
                return False
    
print(is_power(81,9))
#elif b = a**(1/(n+1))
'''