import numpy as np
import MyPack.Math as math

def rho_atm(z,methode="1A"):
# Data from standart atmosphere ( https://www.deleze.name/marcel/physique/TemperaturesEbullition/table_masse_vol.html )
    if methode == "1A":
        rho_list = [
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
        z_list = np.arange(-500,12400,100)
        return math.y_value(rho_list,z_list,z)
