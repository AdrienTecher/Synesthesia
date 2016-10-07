# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:05:44 2016

@author: Adrien
"""

from PIL import Image
from colorsys import rgb_to_hls

#from numpy import array
#import cv2

def color_hue_from_rgb(rgb):
    """
    rgb: the rgb tuple
    
    returns: the hue obtained from rgb
    """
    hls=rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    return hls[0]
    

def imageLoader(image_name):
    """
    image_name: the name of the image to be loaded
    
    returns: tuple (loaded image, height of image, width of image)
    """
    img = Image.open("img/"+image_name)
    return (img.load(), img.size[1], img.size[0])
    

def generateColorArray(image, divs):
    """
    image: tuple (pixel, height, width)
    divs: tuple (number of horizontal divisions, number of vertical divisions)
    
    returns: array of hues extracted from the image
    """
    colors=[]
    for pos_y in range(0,image[1],int(round(image[1]/divs[0]))+10):
        for pos_x in range(0,image[2],int(round(image[2]/divs[1]))+10):
            colors.append(int(round(color_hue_from_rgb(image[0][pos_x,pos_y])*360,0)))
    return colors


def generateColoredPixelImage(image, divs):
    """
    image: tuple (pixel, height, width)
    divs: tuple (number of horizontal divisions, number of vertical divisions)
    
    returns: white image with colored pixels
    """
    img_neg = Image.new( 'RGB', (image[2],image[1]), "white")
    pix_neg = img_neg.load()
    for pos_y in range(0,image[1],int(round(image[1]/divs[0]))+10):
        for pos_x in range(0,image[2],int(round(image[2]/divs[1]))+10):
            pix_neg[pos_x,pos_y]=image[0][pos_x,pos_y]
    return img_neg
    
#To generate image from processed pixel
#
#
#img_name="img_out/img_"+str(name_index)+".jpg"
#Image.new( 'RGB', (width,height), pixel[pos_x,pos_y]).save(img_name)
#name_index+=1
        
def colorsToColorNames(colors):
    """
    colors : array of hue values (int)
    
    returns: array of color names (str)
    """
    color_names=[]
    for color in colors:
        if 355<=color or color<11:
            color_names.append("red")
        elif 11<=color and color<21:
            color_names.append("red_orange")
        elif 21<=color and color<41:
            color_names.append("orange_brown")
        elif 41<=color and color<51:
            color_names.append("orange_yellow")
        elif 51<=color and color<61:
            color_names.append("yellow")
        elif 61<=color and color<81:
            color_names.append("yellow_green")
        elif 81<=color and color<141:
            color_names.append("green")
        elif 141<=color and color<170:
            color_names.append("green_cyan")
        elif 170<=color and color<201:
            color_names.append("cyan")
        elif 201<=color and color<221:
            color_names.append("cyan_blue")
        elif 221<=color and color<241:
            color_names.append("blue")
        elif 241<=color and color<281:
            color_names.append("blue_magenta")
        elif 281<=color and color<321:
            color_names.append("magenta")
        elif 321<=color and color<331:
            color_names.append("magenta_pink")
        elif 331<=color and color<346:
            color_names.append("pink")
        elif 346<=color and color<355:
            color_names.append("pink_red")   
        else:
            color_names.append("error")
    return color_names