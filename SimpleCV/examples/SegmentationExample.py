#!/usr/bin/python
#
import time
from SimpleCV import *
from SimpleCV.Display import Display, pg

display = Display(resolution = (800, 600)) #create a new display to draw images on
cam = Camera() #initialize the camera
done = False # setup boolean to stop the program

count = 0 
#segmentor = ColorSegmentation()
segmentor = DiffSegmentation(threshold=(40,40,40),grayOnly=False);
# Loop until not needed

temp = cam.getImage()
#segmentor.addToModel(temp)
print("Got Image")
while not display.isDone():
    image = cam.getImage() # get image (or frame) from camera
    segmentor.addImage(image)
        
    if(segmentor.isReady()):
        test = segmentor.getSegmentedImage()
        blobs = segmentor.getSegmentedBlobs()
        blobLayer = DrawingLayer((image.width,image.height))
        for b in blobs:
            b.draw(color=Color.GOLD,layer=blobLayer,width=1)
    image.addDrawingLayer(blobLayer)
    image.save(display)
    image.clearLayers()
    time.sleep(0.01) # Let the program sleep for 1 millisecond so the computer can do other things
    if display.mouseLeft:
        display.done = True #if the left arrow is pressed, close the program