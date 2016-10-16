# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:40 2016

@author: Adrien
"""

from numpy import int16,concatenate,empty
from scipy.io.wavfile import write
from pydub import AudioSegment


def generateInstrumentTune(name,color_names, color_note):
    """
    name: name of created wav file
    color_names: list of color names (str)
    color_note : dictionnary that links color names to notes
    
    Creates a wav file containing the generated song
    """
    tune = AudioSegment.silent()
    for color in color_names:
           tune+=color_note[color]
    tune.export(str(name)+".wav", format='wav')
    
    
#adds note to tune 
# pos: 0 to add a note at the end some other integer to add note at the beginning
    
def generateSynthTune(name,color_names, color_note):
    """
    name: name of created wav file
    color_names: list of color names (str)
    color_note : dictionnary that links color names to notes
    
    Creates a wav file containing the generated song
    """
    tune=empty(0,dtype=int16)
    for color in color_names:
        tune=concatenate((tune,color_note[color]))
    write(str(name)+'.wav',44100,tune) # writing the sound to a file


