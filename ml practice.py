# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 20:31:51 2018

@author: Dmob
"""
import numpy as np
import tensorflow as tf
y = np.zeros((3, 3, 4))

print(y.shape[1])

print(11.9//2)  #floor division

print(np.random.rand(3,2))

import sys
print('Hello, Colaboratory from Python {}!'.format(sys.version_info[0]))


with tf.Session():
  input1 = tf.constant(2.0, shape=[2, 3])
  input2 = tf.constant(np.reshape(np.arange(1.0, 7.0, dtype=np.float32), (2, 3)))
  output = tf.add(input1, input2)
  result = output.eval()

print(result)

import matplotlib.pyplot as plt

x = np.arange(20)
y = [x_i + np.random.randn(1) for x_i in x]
a, b = np.polyfit(x, y, 1)
_ = plt.plot(x, y, 'o', np.arange(20), a*np.arange(20)+b, '-')




