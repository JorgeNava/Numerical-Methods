# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:36:22 2020

@author: Jorge Nava
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

def f(x):
  return np.exp(x)

resolution = 500
x = np.linspace(-1,1,resolution)
n=3
y=np.zeros(resolution)
for i in range(0,n):
  y=y+(x**i)/mt.factorial(i)

plt.plot(x,y)
plt.plot(x,f(x))
print(f(x))