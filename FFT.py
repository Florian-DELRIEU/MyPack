"""
Module pour analysse spectrales
"""
import numpy as np

def fft(x):
    return 2*np.fft.fft(x)[0:len(x)//2+1]

def freq(x,t=np.array([])):
    if len(t) == 0: t = np.arange(len(x))
    assert len(t) == len(x) , "x and t vectors must be in same lenght"
    N = len(x)
    fs= N / t[-1] # sampling frequency
    return fs*np.arange(N/2+1)/N