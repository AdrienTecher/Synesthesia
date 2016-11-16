# Synesthesia
Music Generation from Color Recognition

A simple GUI which enables you to analyze the hue of pixels on an image and generates a tune according to the hues. 

List of modules used:

[NumPy](http://www.numpy.org/), [SciPy](https://www.scipy.org/), [PyDub](https://github.com/jiaaro/pydub/), [Pillow](http://python-pillow.org/), [OpenCV](http://opencv.org/) and Tkinter.

##Program Description
The GUI takes in different parameters: the image to analyze, the instrument used for the notes, for the synthesizer the note duration, the number of horizontal and vertical divisions for the image (number of pixels analyzed) and the output name.

###Image processing (Input: image path, number of divisions)
* Loads image
*	Stores the hues of each scanned pixel in a list
*	Output
  * Generates image composed of a white background and the scanned pixels
  *	Associates each hue with the color name
  
###Notes generation (Input: instrument, time)
*	Creating the notes
  *	Synthesizer: Stores all notes in the C4-D5d range by using the sine function and the note frequencies in an array
  *	Other instruments (piano, trumpet, percussions): retrieves pre-ordered audio extracts corresponding to one note and stores in an array
*	Associates each note from the array to a color

###Tune creation
Creates the tune by concatenating the notes from 2-b that correspond to each color in the array (1-c)


##Possible improvements
-	Nice looking GUI
-	Divide the image in areas and averaging the color in that area
-	More varieties of colors
-	Live processing
-	Revert process (music to color)
