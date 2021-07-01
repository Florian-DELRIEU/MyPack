from MyPack.FFT import *
from MyPack.Math import *
import matplotlib.pyplot as plt
import numpy as np

def norm(x,y=None,z=None):
    if y==None and z==None: # si x est seul argument
        x = np.array(x)
        return np.sqrt(np.sum(x**2)) # renvoie la norme N du :array: (somme des carrés)
    if z == None:   return np.sqrt(x**2 + y**2)
    else:           return np.sqrt(x**2 + y**2 + z**2)

def unit(x,y=None,z=None):
    N = norm(x,y,z)
    if y==None and z==None: return np.array(x) / N
    if z == None:           return np.array([x,y]) / N
    if z != None:           return np.array([x,y,z]) / N


U = unit(2,3)
