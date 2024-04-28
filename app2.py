# -*- coding: utf-8 -*-
import cv2
import numpy as np
def dummy(value):
    pass
# read in an image, make a grayscale copy
color_original = cv2.imread('test.jpg')
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)


# create the UI (window and trackbars)
cv2.namedWindow('app')

# arguments: trackbarName, windowName, value (initial value), count (max value), on Change (event handler)
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)

# name=brightness, initial value=50, max value=100, event handler=dummy
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
# Filter bar
cv2.createTrackbar('filter', 'app', 0, 1, dummy)#TO DO: update the scale
# Grayscale bar
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

# main UI loop
while True:
    # To DO: read all the trackbar values
    grayscale = cv2.getTrackbarPos('grayscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    #To do: apply the filters
    # apply the brighness and contrast
    color_modified = cv2.addWeighted(color_original, contrast, np.zeros_like(color_original), 0, brightness - 50)
    gray_modified = cv2.addWeighted(gray_original, contrast, np.zeros_like(gray_original), 0, brightness - 50)
    # wait for keypress (100 milliseconds)
    key = cv2.waitKey(100)
    if key == ord('q'): #function that converts the character into integer
        break
    elif key == ord('s'):
        # To do: save image
        pass
        
    # show the image
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

# Window cleanup
cv2.destroyAllWindows()