import numpy as np
import MyPack.Math as math

def rho_atm(z,methode="1A"):
# Data from standart atmosphere (
    rho_list = [
        1,2,3,4,
        5,6,7
    ]
    z_list = np.arange(-500,20000,100)
    if methode == "1A":
        return math.y_value(rho_list,z_list,z)