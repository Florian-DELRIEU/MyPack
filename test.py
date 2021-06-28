from MyPack.Math import *
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x)

DYDX = (y[1:] - y[:-1])/(x[1:] - x[:-1])

# Regression 
a = (DYDX[-1] - DYDX[-2])/(x[-2] - x[-3])
b = DYDX[-1] - a * x[-2]
last_dydx = a * x[-1] + b
DYDX = np.array( list(DYDX) + [last_dydx])

plt.figure(1)
plt.plot(x,y)
plt.plot(x,DYDX)

plt.show()
