from MyPack.Math import *
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x)

DYDX = (y[1:] - y[:-1])/(x[1:] - x[:-1])

# Regression 
a = (DYDX[-1] - DYDX[-2]) / (x[-1] - x[-2])
b = DYDX[-1] - a * x[-1]
last_dydx = a * x[-1] + b
DYDX = np.array( list(DYDX).copy() + [last_dydx])

plt.figure(1)
plt.clf()
plt.plot(x,y,"+")
plt.plot(x,DYDX,"+")

plt.show()
