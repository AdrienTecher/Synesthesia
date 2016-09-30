# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:02:30 2016

@author: Adrien
"""

from pydub import AudioSegment

sound1 = AudioSegment.from_file("piano_pack/piano_1.wav")
sound2 = AudioSegment.from_file("piano_pack/piano_2.wav")

combined = sound1+sound2

combined.export("pi.wav", format='wav')