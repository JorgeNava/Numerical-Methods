# All regressions
# import libraries

import numpy as np
import math as mt
from matplotlib import pyplot as plt
import pandas as pd

x=np.array([1,1.2,1.5,2,3,3.7,4,4.5])            # x values as a row because in x doesn't matter
y=np.array([[3],[3.4],[5],[2],[4.1],[5],[7],[6.5]]) # y values as a column

k=1                          # To define which regression I want to compute
                               # k=1 linear, k=2 cuadratic, k=3 exponential

n = len(x)                     # Amount of data in our regression

if k==1:
    # linear regression
    M=np.ones((n,2))           # Matrix of ones with order nx2
elif k==2: 
    # cuadratic regression
    M=np.ones((n,3))           # Matrix of ones with order nx2
elif k==3: 
    # exponential regression
    M=np.ones((n,2))           # Matrix of ones with order nx2
else:
    # logarithm regression
    M=np.ones((n,2))           # Matrix of ones with order nx2

b=np.ones((n,1))               # Initializing the matrixes
# Change the columns of M matrix
for i in range(0,n):
    if k==1:
        M[(i),(1)]=x[(i)]
        b=y
    elif k==2:
        M[(i),(1)]=x[(i)]
        M[(i),(2)]=x[(i)]*x[(i)]
        b=y
    elif k==3:
        M[(i),(1)]=x[(i)]
        b[(i)]=mt.log10(y[(i)])
    else:
        M[(i),(1)]=mt.log(x[(i)])
        b[(i)]=mt.log(y[(i)])

Mt = np.transpose(M)      # Transpose Matrix of M
invMtM = np.linalg.inv(np.dot(Mt,M))
Mty = np.dot(Mt,b)
sol = np.dot(invMtM,Mty)

if k==1:
    yf = sol[(0)]+sol[(1)]*x
    print('b',sol[0],'m',sol[1])
elif k==2:
    yf = sol[(0)]+sol[(1)]*x+sol[(2)]*x**2
    print('c',sol[0],'b',sol[1],'a',sol[2])
elif k==3:
    yf = 10**sol[(0)]*10**(sol[(1)]*x)
    print('b: ',sol[(0)],'m: ',sol[(1)])
    print('y ',10**sol[(0)],'*',10**sol[(1)])
else:
    print('~b: ',sol[0])
    sol[(0)] = np.exp(sol[(0)])
    yf = sol[(0)]*x**sol[(1)]
    print('b',sol[0],'m',sol[1])
    
print(y[0]-yf[0])
plt.plot(x,y,'o')
plt.plot(x,yf,'r')
plt.legend(('data','regression'))
plt.xlabel('x')
plt.ylabel('y')



