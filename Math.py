"""
Diverses fonctions et méthode pour des analyses mathématiques
"""
import numpy as np

def norm(x,y=None,z=None):
    """
    Retourne la norme d'un vecteur (x,y,z) ou d'un array (x)
    :param x: coordonés
        - si :array: racine de la somme des carrés
    :param y: , :param z: coordonées
    """
    if y==None and z==None: # si x est seul argument
        x = np.array(x)
        return np.sqrt(np.sum(x**2)) # renvoie la norme N du :array: (somme des carrés)
    if z == None:   return np.sqrt(x**2 + y**2)
    else:           return np.sqrt(x**2 + y**2 + z**2)

def unit(x,y=None,z=None):
    """
    renvoie un vecteur unitaire colinéaire au vecteur argument
    :param x: , :param y: , :param z:
    """
    N = norm(x,y,z)
    if y==None and z==None: return np.array(x) / N
    if z == None:           return np.array([x,y]) / N
    if z != None:           return np.array([x,y,z]) / N

def diff(y,x=None):
    """
    Dérivé par difference finies d'ordre 1
    """
    y = np.array(y)
    x = np.array(x)
    if x.any() == None:
        DYDX = (y[1:] - y[:-1])
        DYDX = np.array( list(DYDX) + [DYDX[-1]] )
    else:
        DYDX = (y[1:] - y[:-1])/(x[1:] - x[:-1]) # len(DXDY) = len(x) - 1
    # Regression linéaire pour le dernier points pour avoir la meme longueur que x
        a = (DYDX[-1] - DYDX[-2])/(x[-2] - x[-3])
        b = DYDX[-1] - a*x[-2]
        last_dydx = a * x[-1] + b
        DYDX = np.array( list(DYDX) + [last_dydx])
    return DYDX

def Integr(f,x=None):
    """
    Intégre la fonction f sur toute la longeur de l'intervalle
    :param f: fonction
    :param x: x
    :return:
    """
    f = np.array(f)
    x = np.array(x)
    if x.any() == None:
        Dx = 1
    else:
        Dx = diff(x)
    I = 0
    for i in np.arange(len(f) - 1):
        I += Dx[i]*(f[i] + f[i + 1])/2
    return I

def primit(f,x=None,CI=0):
    """
    Renvoie la primitive calculé par différence finie
    :param f:
    :param x:
    :param CI: constance d'intégration
    :return:
    """
    f = np.array(f)
    x = np.array(x)
    I = list()
    if x.any() == None:
        i_array = np.arange(len(f))[:-1]
        I.append((f[0] + f[1])/2)
        for i in i_array:
            I.append(Integr(f[:i + 2]))
    else:
        i_array = np.arange(len(x))[:-1]
        I.append((x[1]-x[0])*(f[0] + f[1])/2)
        for i in i_array:
            I.append(Integr(f[:i+2],x[:i+2]))
    return np.array(I)-1
