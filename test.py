import MyPack.Math as m
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
y = np.sin(x)
Y = -np.cos(x)

dx = m.dx(x)

Int = dx * (y[:-1] + y[1:]) / 2

plt.figure(1)
plt.clf()
plt.plot(x,y,"b-",label="f")
plt.plot(x,Y,"b--",label="F")
plt.plot(x[:-1],Int,"r-",label="I")
plt.legend(loc="upper right")

plt.show()

print(m.Integral(y,x))