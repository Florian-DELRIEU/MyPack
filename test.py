from MyPack.Math import *
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,10)
y = x
Y = -np.cos(x)

dydx = diff(x)

plt.figure(1)
plt.clf()
plt.plot(x,y,"b-",label="f")
plt.plot(x,dydx,"b--",label="df")

plt.legend(loc="upper right")
plt.show()
