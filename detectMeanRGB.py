import numpy as np
import cv2
import math
#from PIL import Image

from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv
from math import sqrt


### RGB VALUES FOR IDEAL COLOR CODES
#COLORS = (
#    (255, 221, 53), # Yellow / PANTONE 108 U
#    (151, 169, 38)  # Green  / PANTONE 390 U
#)


### COLORS FOR REAL COLOR CODES
COLORS = (
    (223, 215, 136),    #Yellow indicator
    (159, 191, 153)     #Green indicator
)




def closest_color(r, g, b):
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return (color_diffs)[0][0], (color_diffs)[1][0]






def calculateMeanRGB(inputImage):
    meanBGR = cv2.mean(inputImage)
    current_Rval = round(meanBGR[2])
    current_Gval = round(meanBGR[1])
    current_Bval = round(meanBGR[0])
    return current_Rval, current_Gval, current_Bval


