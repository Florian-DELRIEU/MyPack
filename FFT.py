"""
Module pour analysse spectrales
"""
import numpy as np

def fft(x):
    """
    A utiliser avec :freq: (Fast fourier transform)
    :param x: array a analyser
    :return: array contenant les coefficients de fourrier
    """
    fftx = np.fft.fft(x)
    fftx = 2*fftx[:len(fftx)//2+1]/len(x)
    return fftx

def freq(x,t=np.array([])):
    """
    :param x: array a analyser
    :param t: vecteur temps
    :return: array contenant la plage de fréquence
    """
    if len(t) == 0: t = np.arange(len(x))
    assert len(t) == len(x) , "x and t vectors must be in same lenght"
    N = len(x)
    fs= N / t[-1] # sampling frequency
    return fs*np.arange(N/2+1)/N

def psd(x):
    """
    A utiliser avec :freq:
    :param x: array a analyser
    :return: array contenant les psd
    """
    fftx = fft(x)
    return abs(fftx)

def plot_psd(x,t=np.array([])):
    import matplotlib.pyplot as plt
    plt.ion()
    if len(t)==0:   t=np.arange(len(x))
    else:           pass
    psdx = psd(x)
    f = freq(x,t)
    plt.figure()
    plt.title("PSD of signal")
    plt.ylabel("|fft(x)|")
    plt.xlabel("frequency (Hz)")
    plt.plot(f,psdx)
    plt.grid("both")

def get_freq(x,t):
    psdx = psd(x)
    f = freq(t)
    psdx, f = np.array(psdx), np.array(f) # ensure they are array
    freq_list = list() # frequency and amplitude list
    psd_list = list()
    for _ in np.arange(len(psdx)):
        maxfreqindic = np.where(psdx == np.max(psdx))
        freq_list.append( f[maxfreqindic] )
        psd_list.append(psdx[maxfreqindic])
        f[maxfreqindic] = 0
        psdx[maxfreqindic] = 0
    return freq_list, psd_list

## TEST
t = np.linspace(0,10,100)
x = np.sin(2*np.pi*t)
a,b = get_freq(x,t)