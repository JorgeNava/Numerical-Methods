# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:57:58 2020

@author: Jorge Nava
"""

import math as mt

  
def displayOperations(i,m,x0,x1):  
  print("m = ",round(f(x1),5)," - ",round(f(x0),5))
  print("    ------------------------")
  print("    ",round(x1,5)," - ",round(x0,5))
  print("m",i," = ",round(m,5))
  
  print()
  
  print("x",i+1," = ",round(x1,5)," - ",round(f(x1),5)) 
  print("                    ----------")
  print("                    ",round(m,5))
  print("x",i+1," -> ",round(x2,5))

  
def displayValues(i,x0,x1):
  print("fx",i," = ",f(x1))
  print("fx",i-1," = ",f(x0))
  print("x",i," = ",x1)
  print("x",i-1," = ",x0)
  

def f(x):
    return (-1.4*(x**3))+(x**2)-7
    
print('secant')
niter = 6
x0=0
x1=1



for i in range(1,niter):
    if x1!=x0:
        print("ITERATION #",i)
        #displayValues(i,x0,x1)
        
        m = (f(x1)-f(x0))/(x1-x0)
        x2 = x1-f(x1)/m
        
        #print("m",i," = ",m)
        #print("x",i+1," -> ",x2)
        displayOperations(i,m,x0,x1)

        x0=x1
        x1=x2
        print("============================================")
    else:
        break