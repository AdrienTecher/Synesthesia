# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:40 2016

@author: Adrien
"""

from numpy import int16,concatenate,empty
from scipy.io.wavfile import write

import notes as n
import colors as c
print(n.A4)

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
    
    





def create_tune(color_list):
    tune=empty(0,dtype=int16)
    for color in color_list:
        tune=add_note(n.di[color],tune)
    return tune
#    
    






    
write('music.wav',44100,create_tune(c.color_names)) # writing the sound to a file



