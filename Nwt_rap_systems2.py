## module newtonRaphson2
""" soln = newtonRaphson2(f,x,tol=1.0e-9).
Solves the simultaneous equations f(x) = 0 by
the Newton-Raphson method using {x} as the initial
guess. Note that {f} and {x} are vectors.
"""
import numpy as np
import sympy as sp
import math as mt

from sympy.matrices import *
from sympy import Derivative, diff, simplify

x = sp.Symbol('x')
y = sp.Symbol('y')

u=x**2+x*y-10
v=y+3*x*y**2-57

dudx=u.diff(x)
dudy=u.diff(y)
dvdx=v.diff(x)
dvdy=v.diff(y)
niter=5
X0=Matrix([[1.5],[3.5]])
a=dudx.subs(x,X0[0]).subs(y,X0[1])
for i in range(0,niter):
    J=Matrix([[float(dudx.subs(x,X0[0]).subs(y,X0[1])),float(dudy.subs(x,X0[0]).subs(y,X0[1]))],[float(dvdx.subs(x,X0[0]).subs(y,X0[1])),float(dvdy.subs(x,X0[0]).subs(y,X0[1]))]])
    V=Matrix([[float(u.subs(x,X0[0]).subs(y,X0[1]))],[float(v.subs(x,X0[0]).subs(y,X0[1]))]])
    X=X0-(J.inv())*V
    X0=X
    print(X)
    
