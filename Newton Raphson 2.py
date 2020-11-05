# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:06:38 2020

@author: Jorge Nava
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import lianlg

def u(x,y):
  return x**2+x*y-10

def v(x,y):
  return y+3*x*y*2-57

def dux(x,y):
  return 2*x+y

def duy(x,y):
  return x

def dvx(x,y):
  return 3*y**2

def dvy(x,y):
  return 1+6*x*y

x0 = 1.5
y0 = 3.5

niter = 10

for i in range(niter):
  a = float(dux(x0,y0))
  b = float(duy(x0,y0))
  c = float(dvx(x0,y0))
  d = float(dvy(x0,y0))
  J = np.matrix([[a,b],[c,d]])
  e = float(u(x0,y0))
  f = float(v(x0,y0))
  uv = np.matrix([[e],[f]])
  invJ = lianlg.inv(J)
  X0 = np.matrix([[float(x0)],[float(y0)]])
  X1 = X0 - invJ*uv
  x0 = X1[0]
  x1 = X1[1]
  print("Iteration #",i+1," x= ",x0," y= ",y0)