# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:42:08 2016

@author: Adrien
"""


from numpy import linspace,sin,pi,int16


def note(freq, len, amp=1, rate=44100):
    t = linspace(0,len,len*rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16)


A4 = note(440.00,0.5,amp=10000)
B4 = note(493.88,0.5,amp=10000)
C4 = note(261.63,0.5,amp=10000)
D4 = note(293.66,0.5,amp=10000)
E4 = note(329.63,0.5,amp=10000)
F4 = note(349.23,0.5,amp=10000)
G4 = note(392.00,0.5,amp=10000)

color_note={"red":A4, "pas rouge":B4}