# Root of equations with Newton rapson

import matplotlib.pyplot as plt
import numpy as np
import math as mt

def dislpayValues(i,x0,x1):
  print("x",i," = ",x0)
  print("f(x",i,") = ",f(x0))
  print("f'(x",i,") = ",df(x0))
  print("x",i+1," -> ",x1)


def f(x):
    return mt.exp(x)-x-6

def df(x):
    return mt.exp(x)-1

x0 = 2.5  
# newton rapston star here
print('Newton Rapson')
niter = 4
for i in range(1,niter+1):
    print("ITERATION #",i)
    x1 = x0-f(x0)/df(x0)
    dislpayValues(i,x0,x1)
    x0=x1
    print("===========================================")
