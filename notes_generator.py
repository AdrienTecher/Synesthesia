# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:42:08 2016

@author: Adrien
"""


from numpy import linspace,sin,pi,int16
from pydub import AudioSegment



def note(freq, note_duration, amp=1, rate=44100):
    """
    freq: note frequency
    note_duration: duration in seconds of the note
    amp: amplitude of the note
    rate: sampling rate
    
    returns: synthesized note
    """
    t = linspace(0,note_duration,note_duration*rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16)

def generateSynthNotes(t=1):
    """
    t: note duration (int)
    
    returns: array of notes
    """
    C4 = note(261.63,t,amp=10000) # Do3
    D4 = note(293.66,t,amp=10000) # Ré3
    E4 = note(329.63,t,amp=10000) # Mi3
    F4 = note(349.23,t,amp=10000) # Fa3
    G4 = note(392.00,t,amp=10000) # Sol3
    A4 = note(440.00,t,amp=10000) # La3
    B4 = note(493.88,t,amp=10000) # Si3
    C5 = note(523.25,t,amp=10000) # Do4
    D5 = note(587.33,t,amp=10000) # Ré4
    E5 = note(659.26,t,amp=10000) # Mi4
    F5 = note(698.46,t,amp=10000) # Fa4
    G5 = note(783.99,t,amp=10000) # Sol4
    A5 = note(880.00,t,amp=10000) # La4
    B5 = note(987.77,t,amp=10000) # Si4
    C6 = note(1046.50,t,amp=10000) # Do5
    D6 = note(1174.66,t,amp=10000) # Ré5

    notes=[C4,D4,E4,F4,G4,A4,B4,C5,D5,E5,F5,G5,A5,B5,C6,D6]
    return notes
    

def generateInstrumentNotes(instrument,len=-1):
    """
    returns: dictionnary that assigns color names to notes
    """
    dir="assets/notes/"+instrument+"/"
    len1=0
    len2=-1
    if instrument=="piano" or instrument=="trumpet":
        len2=380
    elif instrument=="flute":
        len1=100
        len2=820
    notes=[]
    for i in range(16):
        notes.append(AudioSegment.from_file(dir+instrument+"_"+str(i)+".wav")[len1:len2])
    return notes


def assignColorToNotes(notes):
    color_keys=["red", 
            "red_orange", 
            "orange_brown",
            "orange_yellow",
            "yellow",
            "yellow_green",
            "green",
            "green_cyan",
            "cyan",
            "cyan_blue",
            "blue",
            "blue_magenta",
            "magenta",
            "magenta_pink",
            "pink",
            "pink_red"]
    
    color_note={}
    for index,color in enumerate(color_keys):
        color_note[color]=notes[index]
    return color_note 