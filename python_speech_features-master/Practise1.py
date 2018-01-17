
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import soundfile as sf
from array import *
import numpy as np
from python_speech_features import mel2hz
from scipy import correlate as corr
#sig=[]
#rate=[]
##sig=np.array([0]*100)
##slist=np.array(sig)
##print(sig)
##
##rate=np.array([0]*100)
##sig = [[0 for x in range(26)] for y in range(10)]
sig={}
#mfcc_feat=np.array([0]*100)
#fbank_feat=np.array([0]*100)
#for i in range(1,9):
mfcc_feat={}
fbank_feat={}
files="i.wav"
print(files)
str1=1
files= files.replace('i', 'str1')
print(files)
(sig,rate) = sf.read("1.wav")
#print(sig[0][1])
#slist[1]=sig
print("sabse bada boss")
#print(sig[0][0])
#print(slist)
mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)


#print(slist)
#plt.plot(sig)
#plt.show()
print(fbank_feat)
n=len(fbank_feat)
print(n)
p=len(fbank_feat.T)
print(p)
print("hello my name")
print(fbank_feat[1][1])
##
##(sig,rate) = sf.read("2.wav")
##mfcc_feat = mfcc(sig,rate)
##fbank_feat = logfbank(sig,rate)
##plt.plot(sig)
##plt.show()
##
##print(fbank_feat[1:3,:])
###plt.plot(sig[2])
####
##(sig,rate) = sf.read("3.wav")
##mfcc_feat = mfcc(sig,rate)
##fbank_feat = logfbank(sig,rate)
####
##print(fbank_feat[1:3,:])
##
##plt.plot(sig)
##plt.show()
##
#print(f)
##plt.plot(sig[2])
##
#print(fbank_feat[5])
##(sig,rate) = sf.read("4.wav")
##mfcc_feat = mfcc(sig,rate)
##fbank_feat = logfbank(sig,rate)
####
##print(fbank_feat[1:3,:])
##plt.plot(sig)
##plt.show()
####
##(sig,rate) = sf.read("5.wav")
##mfcc_feat = mfcc(sig,rate)
##fbank_feat = logfbank(sig,rate)
####
##print(fbank_feat[1:3,:])
##plt.plot(sig)
##plt.show()
##print(fbank_feat[3])
##
#matrix = [[0 for i in range(1)] for j in range(5)]
#print(matrix)
#print("munna bhai mbbs")
#print(mfcc_feat[0][1])
#for i in range(1,3399):
    #r=corr(fbank_feat[i][j],fbank_feat[i+])
 #   print(r)
