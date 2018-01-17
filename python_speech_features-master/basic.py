#!/usr/bin/env python
import soundfile as sf
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import numpy as np
from array import *
from scipy import signal
from scipy import correlate as corr
import numpy as np
##from scipy import fftconvolve
import ffmpy
##from scikit.talkbox import correlations 
##
##ff = ffmpy.FFmpeg(
##inputs={'4.mp3': None},
##outputs={'output.wav': None}
##)
##ff.run()
##ffmpeg.exe -i in.wav -ar 44100  -acodec pcm_s16le  -ac 1 out.wav
(rate,sig) = wav.read("people019_converted.wav")
j=len(sig)
print j
(rate2,sig2) = wav.read("3.wav")
l=len(sig2)
print l
##np.array(sig[1],dtype=float)

######n=len(array)
##print(n)
##p=len(array.T)
##print(p)

mfcc_feat = mfcc(sig,rate)
fbank_feat = logfbank(sig,rate)
mfcc_feat2 = mfcc(sig2,rate2)
print(mfcc_feat[1:3,:])
plt.plot(sig)
plt.show()
print(mfcc_feat2[1:3,:])
plt.plot(sig2)
plt.show
print 'my name is khan'
##(rate,sig) = wav.read("3.wav")
##mfcc_feat = mfcc(sig,rate)
##(rate,sig) = wav.read("3.wav")
##mfcc_feat = mfcc(sig,rate)
##for i in range(1,52):
##    r=corr(mfcc_feat[i],mfcc_feat[i+26],mode='full')
##print(r)
##plt.plot(r)
plt.show()
##for i in range(1,167):
##    for j in range(1,13):
##        r=corr(mfcc_feat,mfcc_feat,mode='same')
##print(r)
##plt.plot(r)
##plt.show()
##print mfcc_feat
##print 'DON NAAM TO YAAD HAI'
n=len(mfcc_feat)
print(n)
p=len(mfcc_feat.T)
print(p)
n2=len(mfcc_feat2)
print(n2)
p2=len(mfcc_feat2.T)
print(p2)
for i in range(1,26):
    r=corr(mfcc_feat[i],mfcc_feat2[i],mode='valid')
##corr = signal.correlate2d(mfcc_feat,mfcc_feat, boundary='symm', mode='full')
##y, x = np.unravel_index(np.argmax(corr), corr.shape) # find the match
##n=acorr()
##r=fftconvolve(mfcc_feat,mfcc_feat[::-1],mode='full')

plt.stem(r,range(26))
plt.xticks(r,range(26))
## import matplotlib.pyplot as plt
##fig, (ax_orig, ax_template, ax_corr) = plt.subplots(1, 3)
##ax_orig.imshow(mfcc_feat, cmap='black')
##ax_orig.set_title('Original')
##ax_orig.set_axis_off()
##ax_template.imshow(mfcc_feat, cmap='gray')
##ax_template.set_title('other')
##ax_template.set_axis_off()
##ax_corr.imshow(corr, cmap='gray')
##ax_corr.set_title('Cross-correlation')
##ax_corr.set_axis_off()
##ax_orig.plot(x, y, 'ro')
plt.show()
