"""
Diverses fonctions et méthode pour des analyses mathématiques
"""
import numpy as np

def norm(x,y,z=None):
    if z == None:
        return np.sqrt(x**2 + y**2)
    else:
        return np.sqrt(x**2 + y**2 + z**2)

def dx(x):
    x = np.array(x)
    dx = x[1:] - x[:-1]
    dx = np.array( list(dx) + list(dx[-1]))
    return dx

def dydx(y,x):
    x = np.array(x)
    y = np.array(y)
    DYDX = (y[1:] - y[:-1])/(x[1:] - x[:-1]) # len(DXDY) = len(x) - 1
    # Regression linéaire pour le dernier points pour avoir la meme longueur que x
    a = (DYDX[-1] - DYDX[-2])/(x[-2] - x[-3])
    b = DYDX[-1] - a*x[-2]
    last_dydx = a * x[-1] + b
    DYDX = np.array( list(DYDX) + [last_dydx])
    return DYDX

def Integral(y,x=None):
    if x == None:
        dx = 1
    else:
        dx = dx(x)
    I = 0
    for i in np.arange(len(y) - 1):
        I += dx[i]*(y[i] + y[i + 1])/2

    return I