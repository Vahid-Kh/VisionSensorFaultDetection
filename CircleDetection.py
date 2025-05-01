import numpy as np
import cv2

from matplotlib import image
from matplotlib import pyplot as plt


def detectCircle(image, minRadius, maxRadius):
    minDist = 80
    param1 = 70  #
    param2 = 30  # This value can be changed to adjust the accuracy of the detection: smaller value -> more false circles
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    """ The measure of blurity decides the sensitivity of model 25 higher than 15 e.g.  """
    blurred = cv2.medianBlur(gray, 15)  # cv2.bilateralFilter(gray,10,50,50)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2,
                               minRadius=minRadius, maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            return i[0],i[1],i[2]




