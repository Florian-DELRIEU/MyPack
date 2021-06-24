from MyPack.FFT import *
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
plt.ion()

case = "test_ifft"

if case == 1: ## Multi fréquence
    f1 = 1
    f2 = 0.1
    fe = 10

    tf = 10
    t = np.linspace(0,tf,1000)
    ts = np.arange(0,tf,1/fe)

    x = lambda t: np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

    x1 = x(t)
    xs = x(ts)
    fs = freq(ts)

    plt.figure("Plot")
    plt.plot(t,x1,"b-",label="signal")
    plt.plot(ts,xs,"k*-",label="mesure")
    plt.xlabel("time")
    plt.legend(loc="upper right")

    plt.figure("PSD")
    plt.semilogy(freq(t),psd(x1),"b-",label="signal")
    plt.semilogy(fs,psd(xs),"k*-",label="mesure")
    plt.xlim([0,fs[-1]])
    plt.legend(loc="upper right")


    plt.show()
    
if case == 2:
    f = 40
    tf = 2
    t = np.linspace(0,tf,500)
    bruit = 0.5
    filtre = 0.3
    
    x = np.sin(2*np.pi*f*t) + bruit*rd.rand(len(t))
    psdx = psd(x)
    psdx_ssb = psdx.copy()
    psdx_ssb[psdx_ssb < filtre] = 0
    psdx_ssb[0] = 0
    
    
    
    plt.figure("Plot")
    plt.clf()
    plt.plot(t,x,"b-",label="signal")
    plt.xlabel("time (s)")
    plt.legend(loc="upper right")
    
    
    plt.figure("PSD")
    plt.clf()
    plt.plot(freq(t),psdx,"b-",label="PSD")
    plt.plot(freq(t),psdx_ssb,"r-",label="sans bruit")
    plt.xlabel("Frequency (Hz)")
    plt.legend(loc="upper right")
    plt.show()
    
if case == 3: ## Influence du nombre de points sur le PSD
    f1 = 1
    f2 = 0.1
    fe = 10

    tf = 10
    t = np.linspace(0,tf,5000)
    t1 = np.linspace(0,tf,100)
    t2 = np.linspace(0,tf,400)
    t3 = np.linspace(0,tf,700)
    t4 = np.linspace(0,tf,1000)

    x = lambda t: np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

    x0 = x(t)
    x1 = x(t1)
    x2 = x(t2)
    x3 = x(t3)
    x4 = x(t4)
    fs1 = freq(t1)
    fs2 = freq(t2)
    fs3 = freq(t3)
    fs4 = freq(t4)

    plt.figure("Plot")
    plt.plot(t,x0,"b-",label="signal")
    plt.plot(t1,x1,"k*-",label="100pts")
    plt.xlabel("time")
    plt.legend(loc="upper right")

    plt.figure("PSD")
    plt.semilogy(freq(t),psd(x0),"b-",label="signal")
    plt.semilogy(fs1,psd(x1),"k-",label="mesure 100 pts")
    plt.semilogy(fs2,psd(x2),"k--",label="mesure 400 pts")
    plt.semilogy(fs3,psd(x3),"k.-",label="mesure 700 pts")
    plt.semilogy(fs4,psd(x4),"k+-",label="mesure 1000 pts")
    plt.legend(loc="upper right")


    plt.show()
    
if case == 4: ## Debruitage
    f = 5
    tf = 2
    t = np.linspace(0,tf,500)
    bruit = 0
    debruit_level = 0.2
    
    x = np.sin(2*np.pi*f*t) + bruit*(2*rd.rand(len(t))-1)
    
    FFTx = np.array(fft(x))
    ReFFTx = np.real(FFTx)
    ImFFTx = np.imag(FFTx)
    
    plt.figure("FFT")
    plt.clf()
    plt.subplot(2,1,1)
    plt.plot(freq(t),ReFFTx,"b-",label="Re(FFT)")
    plt.plot(freq(t),ImFFTx,"r-",label="Im(FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.legend(loc="upper right")
    
    ReFFTx[abs(ReFFTx)<debruit_level] = 0
    ImFFTx[abs(ImFFTx)<debruit_level] = 0
    FFTxssb = ReFFTx + ImFFTx * 1j
    
    plt.plot(freq(t),ReFFTx,"b--+",label="Re(FFT) debruité")
    plt.plot(freq(t),ImFFTx,"r--+",label="Im(FFT) debruité")
    plt.legend(loc="upper right")
    
    x_ssb = ifft(FFTxssb,len(x))
    
    plt.subplot(2,1,2)
    plt.plot(freq(t),psd(x),"b-",label="PSD")
    plt.plot(freq(t),psd(x_ssb),"r-",label="debruit")
    plt.xlabel("Frequency (Hz)")
    plt.legend(loc="upper right")
    plt.show()
        
    plt.figure("Plot")
    plt.clf()
    plt.plot(t,x,"b-",label="signal")
    plt.plot(t,x_ssb,"r-",label="Debruit") ## x_ssb est 2x plus petit que le signal source mais la PSD est correcte 
    plt.xlabel("time (s)")
    plt.legend(loc="upper right")
   
if case == "test_ifft":
    f = 5  # frequence du signal source
    tf = 2 # temps acquisition
    t = np.linspace(0,tf,500)

    x = np.sin(2*np.pi*f*t) # source

# Transformation fft et séparation réel / imaginaire
    FFTx = np.array(fft(x))
    ReFFTx = np.real(FFTx)
    ImFFTx = np.imag(FFTx)

    x1 = ifft(FFTx,len(x))

    plt.figure("Signal")
    plt.clf()
    plt.plot(t,x,"b-",label="Source")
    plt.plot(t,x1,"r-",label="Ifft")
    
    plt.show()