#!/usr/bin/env python

from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import soundfile as sf
from array import *

sig=array('d',[0,1,2,3,4])
rate=array('d',[0,1,2,3,4])

(sig[0],rate[1]) = sf.read("baby-crying-01.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])
plt.plot(sig[0])
(sig,rate) = sf.read("baby-crying-07.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])
plt.plot(sig[1])

plt.show()


