
import datetime
import cv2
import time

nframes = 100000  # Number of pictures to be taken
interval = 60  # Wait before taing next photo
cap = cv2.VideoCapture(0)  # Which camera to use (inbuilt or external)

for i in range(nframes):
    # Get the image from capture
    ret, img = cap.read()

    # For tie stamping the files
    ts = time.time()
    dt = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    captureName = './/Captured Images//img_'+str(i).zfill(6)+'_'+str(dt)+'.png'

    # Store the image on folder
    cv2.imwrite(captureName, img)

    # Wait for this time then take new photo
    time.sleep(interval)

    print(captureName)
