# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:57:09 2016

@author: Adrien
"""
from PIL import Image
from colorsys import rgb_to_hls

from numpy import array
import cv2

def color_hue_from_rgb(rgb):
    hls=rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    return hls[0]
image_name=input("Image file name: ")
img = Image.open("img/"+image_name)
pixel = img.load()

width=img.size[0]
height=img.size[1]

img_neg = Image.new( 'RGB', (width,height), "white")
pix_neg = img_neg.load()


colors=[]

nb_divs=int(input("Number of divisions: "))

name_index=0
for pos_y in range(0,height,int(round(height/nb_divs))+10):
    for pos_x in range(0,width,int(round(width/nb_divs))+10):
        pix_neg[pos_x,pos_y]=pixel[pos_x,pos_y]
        colors.append(int(round(color_hue_from_rgb(pixel[pos_x,pos_y])*360,0)))
        img_name="img_out/img_"+str(name_index)+".jpg"
        Image.new( 'RGB', (width,height), pixel[pos_x,pos_y]).save(img_name)
        name_index+=1




height, width, layers =  array("img_out/img_"+str(name_index)+".jpg").shape

# Create the OpenCV VideoWriter
video = cv2.VideoWriter("img_out/vid.avi", # Filename
                        -1, # Negative 1 denotes manual codec selection. You can make this automatic by defining the "fourcc codec" with "cv2.VideoWriter_fourcc"
                        10, # 10 frames per second is chosen as a demo, 30FPS and 60FPS is more typical for a YouTube video
                        (width,height) # The width and height come from the stats of image1
                        )

# We'll have 30 frames be the animated transition from image1 to image2. At 10FPS, this is a whole 3 seconds
for i in range(0,30):
    img_blend = Image.blend("img_out/img_"+str(name_index)+".jpg", "img_out/img_"+str(name_index+1)+".jpg", i/30.0)

    # Conversion from PIL to OpenCV from: http://blog.extramaster.net/2015/07/python-converting-from-pil-to-opencv-2.html
    video.write(cv2.cvtColor(array(img_blend), cv2.COLOR_RGB2BGR))

# And back from image2 to image1...
for i in range(0,30):
    img_blend2 = Image.blend("img_out/img_"+str(name_index+1)+".jpg", "img_out/img_"+str(name_index)+".jpg", i/30.0)
    video.write(cv2.cvtColor(array(img_blend2), cv2.COLOR_RGB2BGR))

# Release the video for it to be committed to a file
video.release()


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
    

