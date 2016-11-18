import main
import tkinter as tk
from tkinter import filedialog
import cv2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

master = tk.Tk()
master.minsize(width=600, height=350)
master.title("Synesthesia")

def captureImage():
    """
    Shows a webcam frame, allows to save a picture
    """
    cam = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    while(True):
        ret,frame = cam.read() # return a single frame in variable `frame`
        cv2.imshow('img1',frame) #display the captured image
        if cv2.waitKey(1) & 0xFF == ord('d'): #save on pressing 'd' 
            cv2.imwrite('output/camera_picture.png',frame)
            cv2.destroyAllWindows()
            break
    
    cam.release()
    imagePathText.set(dir_path+"\output\camera_picture.png")


#Image Choice Area
frameImage = tk.Frame(master)
frameImage.pack( side = tk.TOP )

frameImageChoice = tk.Frame(master,borderwidth=3,bd=1)
frameImageChoice.pack()

imageText=tk.StringVar()
imageText.set("Image Path : ")
imageLabel= tk.Label(frameImageChoice,textvariable=imageText).grid(pady=10,row=2,column=1)


imagePathText=tk.StringVar()
imagePathText.set("")
imagePathLabel= tk.Label(frameImageChoice,textvariable=imagePathText,relief=tk.SUNKEN).grid(pady=15,row=2,column=2)
def getImagePath():
    global image_path
    image_path=filedialog.askopenfilename(title="Choose an image", filetypes=[('Image files','.png;*.jpg'),('all files','.*')])
    imagePathText.set(image_path)
chooseImageButton = tk.Button(frameImage, text="Choose an image to analyze", command=getImagePath).grid(ipady=10,padx=10,pady=10,row=1,column=1)
cameraButton = tk.Button(frameImage, text="Take a picture with the camera \n(press 'd' to save image)", command=captureImage).grid(ipady=10,padx=10,pady=10,row=1,column=2)

#Options Choice Area
frameOptions = tk.Frame(master)
frameOptions.pack()

#Note Duration Choice
noteDurationText=tk.StringVar()
noteDurationText.set("Select note duration (in seconds) :")
noteDurationLabel= tk.Label(frameOptions,textvariable= noteDurationText).grid(padx=20,pady=10,row=3,column=1)
noteDuration=tk.DoubleVar()
scaleNoteDuration=tk.Scale(frameOptions,variable=noteDuration,orient=tk.HORIZONTAL,from_=0.001,to=1,resolution=0.001,length=200,state=tk.ACTIVE)
scaleNoteDuration.grid(ipady=10,row=3,column=2)


#Instrument Choice
instrument = tk.StringVar(frameOptions)
instrument.set("Synthesizer")

def scaleStatus(self):
    if instrument.get()!="Synthesizer":
        noteDuration.set(0.25)
        scaleNoteDuration.config(state=tk.DISABLED)
    else:
        scaleNoteDuration.config(state=tk.ACTIVE)


instrumentText=tk.StringVar()
instrumentText.set("Choose instrument :")
instrumentLabel= tk.Label(frameOptions,textvariable=instrumentText).grid(padx=20,row=2,column=1)
listInstrument = tk.OptionMenu(frameOptions, instrument,"Synthesizer", "Piano", "Trumpet","Flute", "Percussion",command=scaleStatus).grid(row=2,column=2)




#Horizontal Divisions Choice
hDivsText=tk.StringVar()
hDivsText.set("Select the number of horizontal divisions :")
hDivsLabel= tk.Label(frameOptions,textvariable= hDivsText).grid(padx=20,pady=10,row=4,column=1)
hDivs=tk.DoubleVar()
scaleHDivs=tk.Scale(frameOptions,variable=hDivs,orient=tk.HORIZONTAL,from_=1,to=64,length=150).grid(ipady=10,row=4,column=2)

#Instrument Choice
vDivsText=tk.StringVar()
vDivsText.set("Select the number of vertical divisions :")
vDivsLabel= tk.Label(frameOptions,textvariable= vDivsText).grid(padx=20,pady=10,row=5,column=1)
vDivs=tk.DoubleVar()
scaleVDivs=tk.Scale(frameOptions,variable=vDivs,orient=tk.HORIZONTAL,from_=1,to=64,length=150).grid(ipady=10,row=5,column=2)

#Output Name Choice
name=tk.StringVar()
name.set("")

outputNameText=tk.StringVar()
outputNameText.set("Enter the name of the outputted tune and image :")
outputNameLabel= tk.Label(frameOptions,textvariable= outputNameText).grid(padx=20,pady=10,row=6,column=1)
outputName= tk.Entry(frameOptions,textvariable=name).grid(row=6,column=2)

#Output Directory Choice
frameOutput = tk.Frame(master)
frameOutput.pack()
frameOutputChoice = tk.Frame(master)
frameOutputChoice.pack()

DirectoryText=tk.StringVar()
DirectoryText.set("Output directory path : ")
DirectoryLabel= tk.Label(frameOutputChoice,textvariable=DirectoryText,).grid(pady=10,row=1,column=1)

outputDirectoryPathText=tk.StringVar()
outputDirectoryPathText.set("")
outputDirectoryPathLabel= tk.Label(frameOutputChoice,textvariable=outputDirectoryPathText,relief=tk.SUNKEN).grid(pady=20,row=1,column=2)

def getOutputDirectoryPath():
    global output_dir_path
    output_dir_path=filedialog.askdirectory()
    outputDirectoryPathText.set(output_dir_path)
outputDirButton = tk.Button(frameOutput, text="Choose an output directory", command=getOutputDirectoryPath).grid(ipady=10,pady=10,row=1,column=1)



#Submit button area
frameSubmit = tk.Frame(master)
frameSubmit.pack()

def getValues():
    #vDivsText.set(name.get())
    main.generate(instrument.get().lower(),image_path,noteDuration.get(),hDivs.get(),vDivs.get(),name.get(),output_dir_path)
    
generateButton = tk.Button(frameSubmit, text="Generate", command=getValues).grid(ipadx=20,ipady=5,pady=20,row=2,column=1)



master.mainloop()