import cv2




def returnMarkedBubbles(referenceGlass, currentGlass, threshVal):
    temporaryRefGlass = referenceGlass.copy()
    temporaryCurrGlass = currentGlass.copy()
    refGlass_gray = cv2.cvtColor(temporaryRefGlass, cv2.COLOR_BGR2GRAY)
    refGlass_gray = cv2.GaussianBlur(refGlass_gray, (21, 21), 0)

    currGlass_gray = cv2.cvtColor(temporaryCurrGlass, cv2.COLOR_BGR2GRAY)
    currGlass_gray = cv2.GaussianBlur(currGlass_gray, (21, 21), 0)

    # For each iteration, calculate absolute difference between current frame and reference frame
    difference = cv2.absdiff(currGlass_gray, refGlass_gray)

    # Apply thresholding to eliminate noise
    thresh = cv2.threshold(difference, threshVal, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=5)

    return thresh