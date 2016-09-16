# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:40 2016

@author: Adrien
"""

from numpy import linspace,sin,pi,int16,concatenate
from scipy.io.wavfile import write

# tone synthesis
def note(freq, len, amp=1, rate=44100):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers
 


# A tone, 2 seconds, 44100 samples per second

A4 = note(440,0.5,amp=10000)
D4 = note(293.66,0.5,amp=10000)
E4 = note(329.63,0.5,amp=10000)
F4 = note(349.23,0.5,amp=10000)
G4 = note(392.00,0.5,amp=10000)

music=concatenate((D4,E4,F4,D4,D4,E4,F4,D4,F4,G4,A4,F4,G4,A4))

write('music.wav',44100,music) # writing the sound to a file



