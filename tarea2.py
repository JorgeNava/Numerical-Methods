# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:10:51 2020

@author: Jorge Nava
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt
import sympy as sym


''' Ingreso '''
n=4 
x0 = 0
x  = sym.Symbol('x')
fx = sym.exp(x)


'''' PROCEDIMIENTO '''
k = 0
polinomio = 0
while not (k>n):
  derivada = fx.diff(x,k)
  derivadax0 = derivada.subs(x,x0)
  divisor = np.math.factorial(k)
  terminok = (derivadax0/divisor)*(x-x0)**k
  
  polinomio = polinomio + terminok
  k = k + 1
  
''' SALIDA '''
print(polinomio)