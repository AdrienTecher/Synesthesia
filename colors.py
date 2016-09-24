# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:57:09 2016

@author: Adrien
"""
from PIL import Image
from colorsys import rgb_to_hls

def color_hue_from_rgb(rgb):
    hls=rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    return hls[0]

img = Image.open("color_squares.jpg")
colors=[]
pixel = img.load()
width=img.size[0]
height=img.size[1]
pos_y=int(round(height/2))

for pos_x in range(0,width,int(round(width/8))):
    colors.append(int(round(color_hue_from_rgb(pixel[pos_x,pos_y])*360,0)))

color_names=[]
for color in colors:
    if 355<=color or color<11:
        color_names.append("red")
    elif 11<=color or color<21:
        color_names.append("red_orange")
    elif 21<=color or color<41:
        color_names.append("orange_brown")
    elif 41<=color or color<51:
        color_names.append("orange_yellow")
    elif 51<=color or color<61:
        color_names.append("yellow")
    elif 61<=color or color<81:
        color_names.append("yellow_green")
    elif 81<=color or color<141:
        color_names.append("green")
    elif 141<=color or color<170:
        color_names.append("green_cyan")
    elif 170<=color or color<201:
        color_names.append("cyan")
    elif 201<=color or color<221:
        color_names.append("cyan_blue")
    elif 221<=color or color<241:
        color_names.append("blue")
    elif 241<=color or color<281:
        color_names.append("blue_magenta")
    elif 281<=color or color<321:
        color_names.append("magenta")
    elif 321<=color or color<331:
        color_names.append("magenta_pink")
    elif 331<=color or color<346:
        color_names.append("pink")
    elif 346<=color or color<355:
        color_names.append("pink_red")   
    else:
        color_names.append("error")
    

