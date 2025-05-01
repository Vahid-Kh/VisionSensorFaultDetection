
import numpy as np
import cv2
from CircleDetection import detectCircle
import time
import datetime

cap = cv2.VideoCapture(0)
""" working now """



print("Date time",", ", "Red", "Green", "Blue")
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Coler conversation  to Hue Saturation and lightness
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    """ HSV H:4-24 S:56-255 V: 49-253"""
    lower_hsv = np.array([4, 55, 50])
    upper_hsv = np.array([24, 255, 220])

    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow('frame', result)
    # cv2.imshow('mask', mask)

    """ORIGINAL WORKING CODE"""
    minRad=4
    detected_circles = None
    while detected_circles is None and minRad<50:
        minRad+=1
        # print(minRad)
        circle = detectCircle(frame, minRad, minRad+2)
        cv2.imshow('Original', frame)
        # print(circle)
        if circle is not None:
            # print(minRad)
            """ Original source method - did not work for me"""
            # x, y, r = detected_circles[0].astype(np.int32)
            x = circle[0].astype(np.int32)
            y = circle[1].astype(np.int32)
            r = circle[2].astype(np.int32)


            roi = frame[y - r: y + r, x - r: x + r]

            # generate mask
            width, height = roi.shape[:2]
            mask = np.zeros((width, height, 3), roi.dtype)
            cv2.circle(mask, (int(width / 2), int(height / 2)), r, (255, 255, 255), -1)
            dst = cv2.bitwise_and(roi, mask)
            # filter black color and fetch color values
            data = []
            for i in range(3):
                channel = dst[:, :, i]
                indices = np.where(channel != 0)[0]
                color = np.mean(channel[indices])
                data.append(int(color))

            # opencv images are in bgr format
            blue, green, red = data # (110, 74, 49)
            ts = time.time()
            dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            print(dt, ", ", red, ", ", green, ", ", blue)
            time.sleep(1)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


"""
RGB code to Color

https://convertingcolors.com/

"""



