# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:42:08 2016

@author: Adrien
"""


from numpy import linspace,sin,pi,int16,empty


def note(freq, len, amp=1, rate=44100):
    t = linspace(0,len,len*rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16)
#
#A4 = 440
#C0 = A4*pow(2, -4.75)
#name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
#    
#def pitch(freq):
#    h = round(12*log2(freq/C0))
#    octave = h // 12
#    n = h % 12
#    return name[n] + str(octave)

t=float(input("Duration of each note in seconds: "))


C4 = note(261.63,t,amp=10000)
C4d = note(277.18,t,amp=10000)
D4 = note(293.66,t,amp=10000)
D4d = note(311.13,t,amp=10000)
E4 = note(329.63,t,amp=10000)
F4 = note(349.23,t,amp=10000)
F4d = note(369.99,t,amp=10000)
G4 = note(392.00,t,amp=10000)
G4d = note(415.30,t,amp=10000)
A4 = note(440.00,t,amp=10000)
A4d = note(466.16,t,amp=10000)
B4 = note(493.88,t,amp=10000)
C5 = note(523.25,t,amp=10000)
C5d = note(554.37,t,amp=10000)
D5 = note(587.33,t,amp=10000)
D5d = note(622.25,t,amp=10000)


color_note={"red":C4, 
            "red_orange":C4d, 
            "orange_brown":D4,
            "orange_yellow":D4d,
            "yellow":E4,
            "yellow_green":F4,
            "green":F4d,
            "green_cyan":G4,
            "cyan":G4d,
            "cyan_blue":A4,
            "blue":A4d,
            "blue_magenta":B4,
            "magenta":C5,
            "magenta_pink":C5d,
            "pink":D5,
            "pink_red":D5d,
            "error":empty(0,dtype=int16)}