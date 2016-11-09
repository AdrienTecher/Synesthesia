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
    
    notes=[C4,C4d,D4,D4d,E4,F4,F4d,G4,G4d,A4,A4d,B4,C5,C5d,D5,D5d]
    
    return notes
    
    
    
def generatePianoNotes():
    """
    returns: dictionnary that assigns color names to notes
    """
    dir="assets/notes/piano/"
    color_note=[]
    for i in range(16):
        color_note.append(AudioSegment.from_file(dir+"piano_"+str(i)+".wav")[:380])
    return color_note

def generateTrumpetNotes():
    """
    returns: dictionnary that assigns color names to notes
    """
    dir="assets/notes/piano/"
    color_note=[]
    for i in range(16):
        color_note.append(AudioSegment.from_file(dir+"piano_"+str(i)+".wav")[:380])
    return color_note


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
        print(index)
        color_note[color]=notes[index]
    return color_note 