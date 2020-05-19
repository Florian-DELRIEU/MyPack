"""
Package de fonctions géometriques pour dessins 2D
"""

def Circle(Center=tuple(),Radius=float(),LineStyle="-",Nombre_points=100,LineWidth=0.5):
    """
    Creer un cercle avec un centre et un rayon
    :param Center: tuple (x_centre,y_centre)
    :param Radius: Rayon du cercle
    :param LineStyle:
    :param Nombre_points: Nombre de point pour tracer le cercle
    :param LineWidth:
    """
    import numpy as np
    import matplotlib.pyplot as plt
    x_centre = Center[0]
    y_centre = Center[1]
    theta = np.linspace(0,2*np.pi,Nombre_points)
    x_cercle = x_centre + Radius*np.cos(theta)
    y_cercle = y_centre + Radius*np.sin(theta)
    plt.plot(x_cercle,y_cercle,LineStyle,LineWidth=LineWidth)

