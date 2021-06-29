from MyPack.Math import *
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
f = np.sin(x)
deriv_f = np.cos(x)

dfdx = diff(f,x)

plt.figure(1)
plt.clf()
plt.plot(x,f,"b-",label="f")
plt.plot(x,deriv_f,"b--",label="df")
plt.plot(x,dfdx,"b-x",label="dydx")

plt.legend(loc="upper right")
plt.show()

print("Intrégale : ",Integral(f,x))