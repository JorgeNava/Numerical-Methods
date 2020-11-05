# -*- coding: utf-8 -*-

"""
commentary can be created in python with quotation marks
"""
# or can be created too with hash key
# Commentaries are only for help when we read a code
# This part import some libraries that I need for my code
import numpy as np
# numpy is for mathematics
import matplotlib.pyplot as plt
# matplotlib is for graphics

print('hola mundo')

sx=32 # integer variable
w = 'hola' # string variable
a = 'a'
a0=3.1416 

def f(x):
 return np.sin(x)

def g(x):
 return np.cos(x)

a=f(np.pi)
print(f(np.pi))

x = np.linspace(0,2*np.pi,20)
y = f(x)
plt.plot(x,y)