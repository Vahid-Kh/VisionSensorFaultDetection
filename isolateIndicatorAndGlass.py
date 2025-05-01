from CircleCalculations import areaOfCircle
from CircleDetection import detectCircle
import numpy as np
import cv2
import math
from math import sqrt
# from PIL import Image

from matplotlib import image
from matplotlib import pyplot as plt
from matplotlib.pyplot import hsv
from PIL import Image


def isolateIndicatorAndGlass(inputImage):

    ### Determining the min/max radius of the circles to be detected - THESE VALUE SHOULD BE ALTERED BASED ON THE INPUT IMAGE
    innerCircle_minRadius = 100
    innerCircle_maxRadius = 200
    outerCircle_minRadius = 200
    outerCircle_maxRadius = 350

    tempImage = inputImage.copy()
    ### Detect circles using Hough Circle Transform
    x_inner, y_inner, r_inner = detectCircle(tempImage, innerCircle_minRadius, innerCircle_maxRadius) # For Danfoss images, moisture setup
    x_outer, y_outer, r_outer = detectCircle(tempImage, outerCircle_minRadius, outerCircle_maxRadius) # For Danfoss images, moisture setup

    ### Extract mask for indicator
    mask1 = np.zeros_like(inputImage)
    maskIndicator = cv2.circle(mask1, (x_inner, y_inner), r_inner, (255, 255, 255), -1)

    ### Calculate pixel coordinates for cropping of indicator
    widthHeightOfRect = int((r_inner) / 2)
    indicator_x1 = int(x_inner-widthHeightOfRect)
    indicator_y1 = int(y_inner-widthHeightOfRect)
    indicator_x2 = int(x_inner+widthHeightOfRect)
    indicator_y2 = int(y_inner+widthHeightOfRect)

    ### Extract mask for only glass frame
    invertedIndicatorMask = cv2.bitwise_not(maskIndicator)
    mask2 = np.zeros_like(inputImage)
    fullMaskGlass = cv2.circle(mask2, (x_outer, y_outer), r_outer, (255, 255, 255), -1)
    maskedGlass = cv2.bitwise_and(inputImage, fullMaskGlass)
    isolatedGlass = cv2.bitwise_and(maskedGlass, invertedIndicatorMask)
    maskGlass = cv2.bitwise_and(fullMaskGlass, invertedIndicatorMask)

    return isolatedGlass, maskGlass, indicator_x1, indicator_y1, indicator_x2, indicator_y2









