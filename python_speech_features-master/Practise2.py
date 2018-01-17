
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import soundfile as sf
from array import *
import numpy as np
from python_speech_features import mel2hz
from scipy import correlate as corr
from tinytag import TinyTag
from pydub import AudioSegment
#sig=[]
#rate=[]
sig=np.array([0]*100)
slist=np.array(sig)
print(sig)

##mpg123 -w 5.wav b.mp3
rate=np.array([0]*100)
mfcc_feat=np.array([0]*100)
fbank_feat=np.array([0]*100)
#for i in range(1,9):

#sig = AudioSegment.from_mp3("C:\python27\b.mp3")
#sig= TinyTag.get('1.wav')
(sig,rate) = sf.read("1.wav")
print(sig)
n=len(sig)
print(n)
p=len(sig.T)
print(p)
##s = np.reshape(sig, (np.product(sig.shape),))
sig=sig.revel()
##s=sg[~np.all(sg == 0, axis=1)]
m=len(sig)
print m
k=len(sig.T)
print(k)
##slist[1]=sig
##print(slist)
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)
##
print(slist)
plt.plot(sig)
plt.show()
print(fbank_feat[1:3,:])
o=len(fbank_feat)
print o
o2=len(fbank_feat.T)
print o2

##
####
(sig,rate) = sf.read("2.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)
plt.plot(sig)
plt.show()

print(fbank_feat[1:3,:])
plt.plot(sig[2])

(sig,rate) = sf.read("3.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])

plt.plot(sig)
plt.show()

##print(f)
plt.plot(sig[2])

print(fbank_feat[5])
(sig,rate) = sf.read("8.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)
##
print(fbank_feat[1:3,:])
plt.plot(sig)
plt.show()

##
##(sig,rate) = sf.read("5.mp3")
##mfcc_feat = mfcc(sig,rate)
##fbank_feat = logfbank(sig,rate)
####
##print(fbank_feat[1:3,:])
##plt.plot(sig)
##plt.show()
##print(fbank_feat[3])
####
###matrix = [[0 for i in range(1)] for j in range(5)]
###print(matrix)
##print(mfcc_feat[0][1])
for i in range(1,52):
    r=corr(mfcc_feat[i],mfcc_feat[i+26],mode='full')
print(r)
plt.plot(r)
