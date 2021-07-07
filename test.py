import numpy as np

def rho_atm(z,methode="1B"):
    if methode == "1B":
        rho = np.real( 352.995 * ((1-0.0000225577*z)**(5.25516)) / (288.15 - 0.0065*z) )
        if len(z) > 1:
            z = np.array([z])
            indic = np.where(z>50000)[0]
            rho[indic] = 0
        return  rho

z = np.array([
    30000 , 35000 , 40000 , 50000
])
rho = rho_atm(z)