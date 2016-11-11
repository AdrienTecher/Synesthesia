# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:04:59 2016

@author: Adrien
"""

import notes_generator as n
import image_color_analysis as i
import tune_generator as t
import os 

#img=input("name of image: ")
#hdiv=int(input("horizontal divs: "))
#vdiv=int(input("vertical divs: "))

#divs=(hdiv,vdiv)


#instrument=str(input("instrument: "))


def generate(instrument,image_path,noteDuration,hDivs,vDivs,name,destination):
    divs=(hDivs,vDivs)
    img=i.imageLoader(image_path)
    
    if instrument == "synthesizer":
        notes=n.generateSynthNotes(noteDuration)
        color_note=n.assignColorToNotes(notes)
        color_array=i.generateColorArray(img,divs)
        color_names=i.colorsToColorNames(color_array)
        t.generateSynthTune(name,color_names,color_note)
    else:
        notes=n.generateInstrumentNotes(instrument)
        color_note=n.assignColorToNotes(notes)
        color_array=i.generateColorArray(img,divs)
        color_names=i.colorsToColorNames(color_array)
        t.generateInstrumentTune(name,color_names,color_note)
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.rename(dir_path+"\\"+name+".wav", destination+"/"+name+".wav")
    i.generateColoredPixelImage(img,divs).save(name+"_analyzed_pixels.bmp")
    os.rename(dir_path+"\\"+name+"_analyzed_pixels.bmp", destination+"/"+name+"_analyzed_pixels.bmp")