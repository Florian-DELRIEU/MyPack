"""
Module pour analyse spectrales
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
    return fs*np.arange(N//2+1)/N

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

def debruit(x,debruit_level):
    FFTx = fft(x)
    NFFT = len(FFTx)
    ReFFTx = np.real(FFTx)
    ImFFTx = np.imag(FFTx)
    ReFFTxssb , ImFFTxssb = np.zeros( NFFT ) , np.zeros( NFFT )
    for i,el in enumerate(ReFFTx):
        if el > debruit_level: ReFFTxssb[i] = ReFFTx[i]
    for i,el in enumerate(ImFFTx):
        if el > debruit_level: ImFFTxssb[i] = ImFFTx[i]
    FFTxssb = ReFFTxssb + ImFFTxssb * 1j
    return ifft(FFTxssb,len(x))

def ifft(fftx,n):
    IFFTx = np.fft.ifft(fftx,n=n)
    IFFTx = IFFTx*n
    return IFFTx


###############################################################
def sort_FA(x,t): # Not working
    psd_x = psd(x)
    freq_x = freq(x,t)
    sorted_psd = list()
    sorted_freq = list()
    for _ in psd_x:
        psdmax_indic = np.where(psd_x == np.max(psd_x))
