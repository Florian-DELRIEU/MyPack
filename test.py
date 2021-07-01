from MyPack.FFT import *
import matplotlib.pyplot as plt
import numpy as np

def sort_PSD(t,x):
    freq_t = list(freq(t))
    psd_x = psd(x)

    sorted_psd = list(np.sort(psd_x))
    sorted_freq = list()

    for el in sorted_psd:
        indic = np.where(psd_x == el) # np.where sort un tuple de array
        indic = int(indic[0]) # recupere la valeur en tant qu'entier
        sorted_freq.append(freq_t[indic])

    return (sorted_psd[::-1] , sorted_freq[::-1])


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
plt.plot(f,psd_x,'b-+')

plt.show()

psd_x = list(psd_x)
f = list(f)

PSD_sort , f_sort = sort_PSD(t,x)

print("max frequency",f_sort[:5])
print("max PSD",PSD_sort[:5])