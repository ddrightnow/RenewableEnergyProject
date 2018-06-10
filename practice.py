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



def find(word, letter,index):
    #index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('mango','o',0))