from MyPack.Math import *
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
f = np.sin(x)
deriv_f = np.cos(x)
Int_f = - np.cos(x)

dfdx = diff(f,x)

####### FONCTION PRIMITIVE ################
I = list()
for i in np.arange(len(x))[:-1]:
    I.append(Integr(f[:i+2],x[:i+2]))
I = np.array(I) - 1
###########################################

plt.figure(1)
plt.clf()
plt.plot(x,f,"k-",label="f")
plt.plot(x,deriv_f,"b--",label="df")
plt.plot(x,dfdx,"b-x",label="dydx")
plt.plot(x,Int_f,"r--",label="Int(F)")
plt.plot(x[:-1],I,"r-x",label="F")

plt.legend(loc="upper right")
plt.show()

print("Intrégale : ",Integr(f,x))

