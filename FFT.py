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
    return 2*np.fft.fft(x)[0:len(x)//2+1]

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
    return abs(fftx/len(x))
