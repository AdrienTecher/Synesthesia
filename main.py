# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:04:59 2016

@author: Adrien
"""

import notes_generator as n
import image_color_analysis as i
import tune_generator as t

color_note=n.generateSynthNotes()

img=i.imageLoader(input("name of image: "))
hdiv=int(input("horizontal divs: "))
vdiv=int(input("vertical divs: "))

divs=(hdiv,vdiv)

color_array=i.generateColorArray(img,divs)

color_names=i.colorsToColorNames(color_array)

t.generateSynthTune("mu",color_names,color_note)
i.generateColoredPixelImage(img,divs).show()