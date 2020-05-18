"""
Package de fonctions géometriques pour dessins 2D
"""

def Circle(Center=tuple(),Radius=float()):
    import numpy as np
    import matplotlib.pyplot as plt
    x_centre = Center[0]
    y_centre = Center[1]
    theta = np.linspace(0,2*np.pi,100)
    x_cercle = x_centre + Radius*np.cos(theta)
    y_cercle = y_centre + Radius*np.sin(theta)
    plt.plot(x_cercle,y_cercle,'-')

import matplotlib.pyplot as plt
plt.figure()
Circle((0,0),2)
plt.show()