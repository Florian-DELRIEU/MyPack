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
    return x[1:] - x[:-1]

def dxdy(x,y):
    x = np.array(x)
    y = np.array(y)
    return (x[1:] - x[:-1]) / (y[1:] - y[:-1])