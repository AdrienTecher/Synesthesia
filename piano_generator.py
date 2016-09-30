# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:34:41 2016

@author: Adrien
"""

from pydub import AudioSegment
import colors as c



combined = AudioSegment.silent()


color_note={"red":AudioSegment.from_file("piano_pack/piano_1.wav")[:200], 
            "red_orange":AudioSegment.from_file("piano_pack/piano_2.wav")[:200], 
            "orange_brown":AudioSegment.from_file("piano_pack/piano_3.wav")[:200],
            "orange_yellow":AudioSegment.from_file("piano_pack/piano_4.wav")[:200],
            "yellow":AudioSegment.from_file("piano_pack/piano_5.wav")[:200],
            "yellow_green":AudioSegment.from_file("piano_pack/piano_6.wav")[:200],
            "green":AudioSegment.from_file("piano_pack/piano_7.wav")[:200],
            "green_cyan":AudioSegment.from_file("piano_pack/piano_8.wav")[:200],
            "cyan":AudioSegment.from_file("piano_pack/piano_9.wav")[:200],
            "cyan_blue":AudioSegment.from_file("piano_pack/piano_10.wav")[:200],
            "blue":AudioSegment.from_file("piano_pack/piano_11.wav")[:200],
            "blue_magenta":AudioSegment.from_file("piano_pack/piano_12.wav")[:200],
            "magenta":AudioSegment.from_file("piano_pack/piano_13.wav"),
            "magenta_pink":AudioSegment.from_file("piano_pack/piano_14.wav")[:200],
            "pink":AudioSegment.from_file("piano_pack/piano_15.wav")[:200],
            "pink_red":AudioSegment.from_file("piano_pack/piano_16.wav")[:200]
            #"error":empty(0,dtype=int16)
            }
            
            

for color in c.color_names:
        combined+=color_note[color]
combined.export("pi.wav", format='wav')