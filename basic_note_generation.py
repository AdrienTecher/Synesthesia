# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:40 2016

@author: Adrien
"""

from numpy import linspace,sin,pi,int16,concatenate,empty
from scipy.io.wavfile import write
#from colorsys import rgb_to_hls
def note(freq, len, amp=1, rate=44100):
    t = linspace(0,len,len*rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16) # two byte integers
 

#adds note to tune 
# pos: 0 to add a note at the end some other integer to add note at the beginning
def add_note(note,tune=empty(0,dtype=int16),pos=0):
    if tune.size==0:
        return note
    else:
        if pos!=0:
            tune=concatenate((note,tune))
        else:
            tune=concatenate((tune,note))
        return tune
    
    

A4 = note(440.00,0.5,amp=10000)
B4 = note(493.88,0.5,amp=10000)
C4 = note(261.63,0.5,amp=10000)
D4 = note(293.66,0.5,amp=10000)
E4 = note(329.63,0.5,amp=10000)
F4 = note(349.23,0.5,amp=10000)
G4 = note(392.00,0.5,amp=10000)



#def color_hue_from_rgb(rgb):
#    hls=rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
#    return hls[0]
colors=[0]
def create_tune(colors):
    tune=empty(0,dtype=int16)
    for color in colors:
        if color==0:
            tune=add_note(tune,A4)
        elif color==1:
            tune=add_note(tune,B4)
        elif color==2:
            tune=add_note(tune,C4)
    return tune
#    
    
colors=[0,1,2,0,1,2,1,0,2,1,2]
#colors.append(color_hue_from_rgb(rgb))

    
write('music.wav',44100,create_tune(colors)) # writing the sound to a file



