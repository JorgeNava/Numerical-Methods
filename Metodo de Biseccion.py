# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:47:22 2020

@author: Jorge Nava
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return x*np.log(x)-2

a = 1
b = 3
niter = 100

for i in range(0,niter):
  c = (a+b)/2
  #Si hay un cambio de signo entre las funciones
  if f(c)*f(a) < 0:
    #Se cambian los limites
    b = c
  else:
    a = c
  print(c)
  print(f(c))
  
  x = np.linspace(1,3,10)
  y = f(x)
  
  plt.plot(x,y)
  plt.plot(c,f(c))