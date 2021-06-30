from MyPack.FFT import *
import matplotlib.pyplot as plt
import numpy as np

def sort_PSD(t,x):
    freq_t = freq(t)
    psd_x = psd(x)

    sorted_psd = np.sort(psd_x)
    sorted_freq = list()

    for el in sorted_psd:
        indic = np.where(psd_x == el)
        sorted_freq.append(freq_t[indic])


f1 , f2 = 10, 15
t = np.linspace(0,1,50)
x = np.sin(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t)

f = freq(t)
psd_x = psd(x)

plt.figure(1)
plt.clf()
plt.plot(t,x)

plt.figure(2)
plt.clf()
plt.plot(f,psd_x)

plt.show()

psd_x = list(psd_x)
f = list(f)