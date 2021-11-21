import numpy as np
import Math as math

# Physical datas
G = 6.674e-11 #N m^2/kg^2 (newton square meters per kilogram squared)
Earth_mass  = 5.97e24  #kg (kilograms)
Moon_mass   = 7.35e22  #kg (kilograms)
Sun_mass    = 1.99e30  #kg (kilograms)
T0          = -273.15   #K
C_light     = 2.998e8  #m/s (meters per second)
C_sound     = 340.27    #m/s (meters per second)  (condition standart)

def rho_atm(z,methode="1B"):
# Data from standart atmosphere ( https://www.deleze.name/marcel/physique/TemperaturesEbullition/table_masse_vol.html )
    if methode == "1A":
        z_list = np.arange(-500,12400,100)
        if z >= max(z_list):
            return 0
        rho_list = [ # z = np.arange(-500,12400,100)
            1.285, 1.273, 1.261, 1.249, 1.237,
            1.225, 1.213, 1.202, 1.190, 1.179,
            1.167, 1.156, 1.145, 1.134, 1.123,
            1.112, 1.101, 1.090, 1.079, 1.069,
            1.058, 1.048, 1.037, 1.027, 1.017,
            1.007, 0.996, 0.986, 0.977, 0.967,
            0.957, 0.947, 0.938, 0.928, 0.919,
            0.909, 0.900, 0.891, 0.881, 0.872,
            0.863, 0.854, 0.845, 0.837, 0.828,
            0.819, 0.811, 0.802, 0.794, 0.785,
            0.777, 0.769, 0.760, 0.752, 0.744,
            0.736, 0.728, 0.720, 0.713, 0.705,
            0.697, 0.690, 0.682, 0.675, 0.667,
            0.660, 0.652, 0.645, 0.638, 0.631,
            0.624, 0.617, 0.610, 0.603, 0.596,
            0.590, 0.583, 0.576, 0.570, 0.563,
            0.557, 0.550, 0.544, 0.538, 0.531,
            0.525, 0.519, 0.513, 0.507, 0.501,
            0.495, 0.489, 0.484, 0.478, 0.472,
            0.466, 0.461, 0.455, 0.450, 0.444,
            0.439, 0.434, 0.428, 0.423, 0.418,
            0.413, 0.408, 0.403, 0.398, 0.393,
            0.388, 0.383, 0.378, 0.373, 0.369,
            0.364, 0.359, 0.355, 0.350, 0.346,
            0.341, 0.337, 0.333, 0.328, 0.324,
            0.320, 0.316, 0.311, 0.307, 0.303
        ]
        return math.y_value(rho_list,z_list,z)
# Modele math issue du website (https://www.deleze.name/marcel/physique/TemperaturesEbullition/table_masse_vol.html)
    if methode == "1B":
    # Modele math de la methode "1A"
        rho = np.real( 352.995 * ((1-0.0000225577*z)**(5.25516)) / (288.15 - 0.0065*z) )
        if type(z) == np.ndarray:
            rho[np.where(np.isnan(rho))] = 0  # si ==nan alors =0
            rho[np.where(rho <= 1e-5)] = 0  # si inf à 1e-5 alors =0
        elif rho <= 1e-5 or np.isnan(rho):
            rho = 0
        return rho

def sound_speed(T,M,gamma=7/5): pass

def Temp_atm(z,methode="1A"):
    """
    FIXME
    TODO
        - add rho_list
    :param z: Altutide (en m)
    :param methode: Méthode de calcul
    """
    if methode == "1A":
        temp_list = [
            18.3, 17.6, 17.0, 16.3, 15.7,
            15.0, 14.4, 13.7, 13.1, 12.4,
            11.8, 11.1, 10.5, 9.8, 9.1,
            8.5, 7.9, 7.2, 6.5, 5.9,
            5.3, 4.6, 4.0, 3.3, 2.7,
            2.0, 1.4, 0.7, 0.1, -0.6,
            - 1.3, -1.9, -2.6, -3.2, -3.8,
            - 4.5, -5.2, -5.8, -6.4, -7.1,
            - 7.8, -8.4, -9.1, -9.7, -10.4,
            - 11.0, -11.7, -12.3, -13.0, -13.6,
            - 14.3, -14.9, -15.6, -16.2, -16.9,
            - 17.5, -18.2, -18.8, -19.5, -20.1,
            - 20.8, -21.4, -22.1, -22.7, -23.4,
            - 24.0, -24.7, -25.3, -26.0, -26.6,
            - 27.3, -27.9, -28.6, -29.2, -29.9,
            - 30.5, -31.2, -31.8, -32.5, -33.1,
            - 33.8, -34.4, -35.1, -35.7, -36.4,
            - 37.0, -37.7, -38.3, -39.0, -39.6,
            - 40.3, -40.9, -41.5, -42.2, -42.9,
            - 43.5, -44.2, -44.8, -45.5, -46.1,
            - 46.8, -47.4, -48.1, -48.7, -49.4,
            - 50.0, -50.7, -51.3, -52.0, -52.6,
            - 53.3, -53.9, -54.6, -55.2, -55.9,
            - 56.5, -57.1, -57.8, -58.5, -59.1,
            - 59.8, -60.4, -61.1, -61.7, -62.4,
            - 63.0, -63.6, -64.3, -65.0, -65.6  ]
        z_list = np.arange(-500, 12400, 100)
        assert type(z) is not np.ndarray , "Z can't be an array"
        if z >= max(z_list):
            return None
        rho_list = []
        return math.y_value(rho_list,z_list,z)
