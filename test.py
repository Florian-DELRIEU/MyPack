from MyPack.Math import *
import matplotlib.pyplot as plt

x = np.linspace(0,54,3)
y = x

dx = dx(x)


I = 0
for i in np.arange(len(y)-1):
    I += dx[i] * (y[i] + y[i+1])/2

print(I)
