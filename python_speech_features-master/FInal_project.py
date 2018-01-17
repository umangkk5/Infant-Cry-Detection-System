#!/usr/bin/env python
import soundfile as sf
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import numpy as np
from array import *
from scipy import signal
from scipy.signal import correlate2d as corr
import numpy as np
##from scipy import fftconvolve
import ffmpy

##def corr2_coeff(A,B):
##    # Rowwise mean of input arrays & subtract from input arrays themeselves
##    A_mA = A - A.mean(1)[:,None]
##    B_mB = B - B.mean(1)[:,None]
##
##    # Sum of squares across rows
##    ssA = (A_mA**2).sum(1);
##    ssB = (B_mB**2).sum(1);
##
##    # Finally get corr coeff
##    return np.dot(A_mA,B_mB.T)/np.sqrt(np.dot(ssA[:,None],ssB[None]))


(rate,sig) = wav.read("people019_converted.wav")
##sig=s.flatten()
##sig=np.ravel(s)
(rate3,sig3) = wav.read("3.wav")
(rate4,sig4) = wav.read("baby-crying-01_converted.wav")
(rate5,sig5) = wav.read("Baby_cry_2.wav")
j=len(sig)
print j
j2=len(sig.T)
print j2


(rate2,sig2) = wav.read("3.wav")
l=len(sig2)
print l
l2=len(sig2.T)
print l2

mfcc_feat = mfcc(sig,rate)
mfcc_feat2 = mfcc(sig2,rate2)
mfcc_feat3 = mfcc(sig3,rate3)
mfcc_feat4 = mfcc(sig4,rate4)
mfcc_feat5 = mfcc(sig5,rate5)
print(mfcc_feat[1:3,:])
plt.plot(sig)
plt.show()
print(mfcc_feat2[1:3,:])
plt.plot(sig2)
plt.show
print(mfcc_feat3[1:3,:])
##plt.plot(sig3)
##plt.show
print(mfcc_feat4[1:3,:])
##plt.plot(sig4)
##plt.show

n=len(mfcc_feat)
print 'No. of rows in input test sample Cepstrum coefficients'
print(n)
p=len(mfcc_feat.T)
print 'No. of columns in input test sample Cepstrum coefficients'
print(p)
n2=len(mfcc_feat2)
print 'No. of rows of database signal Cepstrum coefficients'
print(n2)
p2=len(mfcc_feat2.T)
print 'No. of column of database signal Cepstrum coefficients'
print(p2)
##r=corr2_coeff(mfcc_feat,mfcc_feat2)
##plt.stem(r,range(26))
out=np.dot(mfcc_feat,mfcc_feat2.T)

##print out
plt.plot(out)

plt.show()
##plt.xticks(r,range(26))
##fig, ax = plt.subplots(2, 1)
##ax[0].plot(sig)
##ax[0].set_xlabel('Time')
##ax[0].set_ylabel('Amplitude')
##ax[1].plot(sig,'r') # plotting the spectrum
##ax[1].set_xlabel('Freq (Hz)')
##ax[1].set_ylabel('|Y(freq)|')
h=len(out)
##
##print h
h2=len(out.T)
sp=np.sum(out)
s=sp/(h*h2)
print 'average correlation value:'
print s
##o=any(out > 2500 for out in out.itervalues())
##for i in range(1,h):
##options = sorted(out.items(), key=lambda e: e[1], reverse=True) # rank from max to min
##if options[0][1] > 2500:
##    print 'infant che bhai'
##    
##    
##else:
##    print 'adult'
##    
if (s>-100):
    print 'this is an infant cry'
else:
    print 'this is an adult speech'
