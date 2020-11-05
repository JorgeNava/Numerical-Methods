# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:10:51 2020

@author: Jorge Nava
"""

""" Library for advanced mathematics """
import numpy as np
""" Library for advanced mathematics """
import math as mt

# numpy y math son librerias similares, la diferencia es quien las programo, pero esencialmente hacen lo mismo
""" Library for plotting results """
import matplotlib.pyplot as plt
''' On defining functions '''
# se define la funcion analitica 1 que corresponde a 1 entre x
def fana1(x):
    return 1/x
# se define la funcion analitica 2 que corresponde al seno de x
def fana2(x):
    return np.sin(x)

''' number of terms in the Taylor's series '''
# Cuantos terminos se desean agregar a la serie de Taylor?
niter=20

''' varibables Para la funcion 1 '''
a=2
x = np.linspace(1,4,80)
f = (x-a)
# Se inicializa en cero la sumatoria
p=0*f
''' varibables Para la funcion 2 '''
a2=0
x2= np.linspace(-18.14,18.14,80)
f2= (x2-a2)
# Se inicializa en cero la sumatoria
p2=0*f

# Dentro de este bucle for, se suma los terminos de la serie de Tauylor
for i in range(0,niter):
    p=p+(((-1)**i)*f**i)/(a**(i+1))   # Para la serie de f(x)=1/x
    pot=2*i+1
    p2=p2+(((-1)**i)*f2**pot)/(mt.factorial(pot))   # Para la serie de f(x)=sin(x)
    
# Definiendo las funciones analiticas para su grafica y comparacion
yana1=fana1(x)
yana2=fana2(x2)

''' Grafica para f(x)=1/x '''
plt.plot(x,yana1)   # Grafica de funcion analitica
plt.plot(x,p,'or')  # Grafica de la serie de Taylor
plt.grid()
plt.show()

''' Grafica para f(x)=sin(x) '''
plt.ylim(top=2)
plt.ylim(bottom=-2)
plt.plot(x2,yana2)    # Grafica de funcion analitica
plt.plot(x2,p2,'or')  # Grafica de la serie de Taylor  'or' significa que se grafica mediante puntos rojos
plt.grid()
plt.show()