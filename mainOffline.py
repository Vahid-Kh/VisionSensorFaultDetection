import cv2
import numpy as np

# Read image.

# List of test samples for circle color detection
img_l = [
    cv2.imread('Sight glass pictures/sa - Copy.png'),
    cv2.imread('Sight glass pictures/training/WET/SightGlass1_0pct-40.png'),
    cv2.imread('Sight glass pictures/training/DRY/SightGlass21_100pct_10.png'),
    cv2.imread('Sight glass pictures/test.png'),
    cv2.imread('Sight glass pictures/2022-08-30 11_19_14-.png'),
    cv2.imread('Sight glass pictures/Untitled.png'),
    cv2.imread('Sight glass pictures/Untitled - Copy.png'),
    cv2.imread('Sight glass pictures/SightGlass1_0pct-30.png'),
    cv2.imread('Sight glass pictures/sa.png'),
    cv2.imread('Sight glass pictures/sample1.png'),
    cv2.imread('Sight glass pictures/sample2.png'),
    cv2.imread('Sight glass pictures/sample3.png'),
    cv2.imread('Sight glass pictures/sample4.png'),
]

# Iterate over each image in the list
for img in img_l:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale.
    """ 3 different modes of bluring  """

    # Apply median blur to the grayscale image
    gray_blurred = cv2.medianBlur(gray, 15)
    # gray_blurred = cv2.blur(gray, (18, 12))  # Blur using 3 * 3 kernel.
    # gray_blurred = cv2.bilateralFilter(gray,9,75,75)

    # Apply Hough transform on the blurred image to detect circles
    minRad = 20
    detected_circles = None
    # Incrementally increase the minimum radius until circles are detected
    while detected_circles is None:
        minRad += 5
        # print(minRad)
        detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1.2, 20, param1=70, param2=30, minRadius=minRad, maxRadius=minRad + 2)
    # detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1.89, 50, param1=74, param2=30, minRadius=79, maxRadius=88)

    """ Original source method"""
    # gray_blurred = cv2.blur(gray, (3, 3)) # Blur using 3 * 3 kernel.
    # detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT, 1.2, 20, param1 = 50, param2 = 30, minRadius = 30, maxRadius = 50)  # Apply Hough transform on the blurred image.

    # Draw circles that are detected.
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        # Iterate over each detected circle
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

        # Display the image with detected circles
        cv2.imshow("Detected Circle", img)

    if detected_circles is not None:
        """ Original source method - did not work for me"""
        # Extract the first detected circle's parameters
        x = detected_circles[0][0][0].astype(np.int32)
        y = detected_circles[0][0][1].astype(np.int32)
        r = detected_circles[0][0][2].astype(np.int32)
        # Define region of interest (ROI) around the detected circle
        roi = img[y - r: y + r, x - r: x + r]
        # Generate a mask for the ROI
        width, height = roi.shape[:2]
        mask = np.zeros((width, height, 3), roi.dtype)
        cv2.circle(mask, (int(width / 2), int(height / 2)), r, (255, 255, 255), -1)
        # Apply the mask to the ROI to isolate the circle
        dst = cv2.bitwise_and(roi, mask)
        # Filter out black color and fetch color values
        data = []
        for i in range(3):
            channel = dst[:, :, i]
            indices = np.where(channel != 0)[0]
            color = np.mean(channel[indices])
            data.append(int(color))

        # Extract BGR color values from the data
        blue, green, red = data  # (110, 74, 49)
        # Print the extracted color values
        print(red, green, blue)

    # Wait for a key press to proceed to the next image
    cv2.waitKey(0)

"""
RGB code to Color
https://convertingcolors.com/
"""