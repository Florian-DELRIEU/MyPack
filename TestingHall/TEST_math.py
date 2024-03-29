# sourcery skip: switch
from MyPack2.Math import *
from MyPack2.FFT import fft,psd,freq
import matplotlib.pyplot as plt
import numpy as np
rd = np.random

TESTING_CASE = "FFT"

if TESTING_CASE == "Partial Mean 1":
    t = np.linspace(0,1,200)
    f = np.cos(t) + rd.random(200)*0.1
    f1_mean = partial_mean(f,100)
    f2_mean = partial_mean(f,50)
    f3_mean = partial_mean(f,10)
    f4_mean = partial_mean(f,5)


    plt.figure(1)
    plt.plot(t,f,label="f1")
    plt.plot(t,f1_mean,label="meaned by 100")
    plt.plot(t,f2_mean,label="meaned by 50")
    plt.plot(t,f3_mean,label="meaned by 10")
    plt.plot(t,f4_mean,label="meaned by 5")
    plt.legend(loc="best")
    plt.grid("both")

elif TESTING_CASE == "FFT":
    t = np.linspace(0,10,100)
    f = np.cos(2*np.pi*1*t)
    freq = freq(t,f)

    PSD = psd(f)
    plt.plot(freq,PSD)