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
    return fftx

def freq(t=np.array([]),x=np.array([])):
    """
    :param t: vecteur temps
    :param x: array a analyser (optionnel)
    :return: array contenant la plage de fréquence

    Attention ⚠ la fonction à été modifiée dans le `commit ...` cela peut causer des erreurs pour des utilisation antérieures
    """
    if len(t) == 0: t = np.arange(len(x))
    N = len(t)
    fs = N/t[-1]  # sampling frequency
    return fs*np.arange(N/2 + 1)/N

def psd(x):
    """
    A utiliser avec :freq:
    :param x: array a analyser
    :return: array contenant les psd
    """
    fftx = np.fft.fft(x)
    fftx = 2*fftx[:len(fftx)//2 + 1]/len(x)
    return abs(fftx)

def plot_psd(x,t=np.array([])):
    """
    Affiche directement la PSD du signal dans une fenêtre prédéfinie
    :param x: signal
    :param t: vecteur temps (optionnnel)
    :return: figure avec la PSD du signal
    """
    import matplotlib.pyplot as plt
    plt.ion()
    if len(t)==0:   t=np.arange(len(x))
    else:           pass
    psdx = psd(x)
    f = freq(t,x)
    plt.figure()
    plt.title("PSD of signal")
    plt.ylabel("|fft(x)|")
    plt.xlabel("frequency (Hz)")
    plt.plot(f,psdx)
    plt.grid("both")

def debruit(x,debruit_level):
    """
    Débruite le signal :x:
    :param x: signal a débruiter
    :param debruit_level: puissance du bruit à filtrer
    :return:
    """
# FFT et séparation réel et imaginaire
    debruit_level *= len(x)/2 # car fft n'est pas normé
    FFTx = np.fft.fft(x)
    ReFFTx = np.real(FFTx)
    ImFFTx = np.imag(FFTx)
# Debruitage et reconstitution
    ReFFTx[abs(ReFFTx)<debruit_level] = 0
    ImFFTx[abs(ImFFTx)<debruit_level] = 0
    FFTxssb = ReFFTx + ImFFTx * 1j
    return ifft(FFTxssb,len(x))

def ifft(fftx,n):
    """
    Reconstitue un signal depuis une FFT
    :param fftx:
    :param n: longeueur du signal voulue
    """
    IFFTx = np.fft.ifft(fftx,n=n)
    return IFFTx


###############################################################
def sort_FA(x,t): # Not working
    psd_x = psd(x)
    freq_x = freq(t,x)
    sorted_psd = list()
    sorted_freq = list()
    for _ in psd_x:
        psdmax_indic = np.where(psd_x == np.max(psd_x))
