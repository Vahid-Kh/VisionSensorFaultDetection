import numpy as np
import cv2
from CircleDetection import detectCircle
import time
import datetime

# Initialize video capture from the default camera (index 0)
cap = cv2.VideoCapture(0)
""" working now """

# Print header for the output data
print("Date time", ", ", "Red", "Green", "Blue")

# Start an infinite loop to continuously capture frames from the camera
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    # Get the width and height of the captured frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Convert the captured frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    """ HSV H:4-24 S:56-255 V: 49-253"""
    # Define the lower and upper bounds for the HSV values to create a mask
    lower_hsv = np.array([4, 55, 50])
    upper_hsv = np.array([24, 255, 220])

    # Create a mask using the defined HSV range
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    # Apply the mask to the original frame to isolate the desired regions
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # Uncomment the following lines to display the result and mask
    # cv2.imshow('frame', result)
    # cv2.imshow('mask', mask)

    """ORIGINAL WORKING CODE"""
    # Initialize minimum radius for circle detection
    minRad = 4
    detected_circles = None
    # Attempt to detect circles with increasing radius until one is found or max radius is reached
    while detected_circles is None and minRad < 50:
        minRad += 1
        # Detect circles in the frame using the current radius range
        circle = detectCircle(frame, minRad, minRad + 2)
        # Display the original frame
        cv2.imshow('Original', frame)
        # If a circle is detected, process it
        if circle is not None:
            # Extract circle parameters: x, y coordinates and radius
            x = circle[0].astype(np.int32)
            y = circle[1].astype(np.int32)
            r = circle[2].astype(np.int32)

            # Define region of interest (ROI) around the detected circle
            roi = frame[y - r: y + r, x - r: x + r]

            # Generate a mask for the ROI
            width, height = roi.shape[:2]
            mask = np.zeros((width, height, 3), roi.dtype)
            cv2.circle(mask, (int(width / 2), int(height / 2)), r, (255, 255, 255), -1)
            # Apply the mask to the ROI to isolate the circle
            dst = cv2.bitwise_and(roi, mask)
            # Filter out black color and fetch color values from the circle
            data = []
            for i in range(3):
                channel = dst[:, :, i]
                indices = np.where(channel != 0)[0]
                color = np.mean(channel[indices])
                data.append(int(color))

            # Extract BGR color values from the data
            blue, green, red = data
            # Get the current timestamp and format it
            ts = time.time()
            dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            # Print the timestamp and color values
            print(dt, ", ", red, ", ", green, ", ", blue)
            # Pause for 1 second before the next iteration
            time.sleep(1)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

"""
RGB code to Color

https://convertingcolors.com/

"""