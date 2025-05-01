Sight Glass Fault Detection Using Camera
This GitHub repository contains the designed solutions for "Vision-based Refrigerant Quality Detection." The project aims to develop a system capable of monitoring a sight glass within a refrigeration system to detect moisture levels and the presence of vapor bubbles in the liquid line.

Classical Approach
The classical approach involves sequential manipulation of images to isolate regions of interest, specifically the glass frame of the sight glass and the indicator.

Moisture Level Detection: This is achieved by extracting a rectangular image of the indicator, focusing on colored pixels. The average RGB value of these pixels is compared to reference colors (green and yellow) to calculate the percentage of yellow, indicating the moisture level.

Vapor Bubble Detection: This method compares the captured image to a reference image with no vapor bubbles and the most recent captured image to account for light fluctuations. Images are compared using a threshold to identify pixels with significant variance, which are then dilated to accurately quantify bubble size.

Current Implementation
Currently, the solution is not designed for real-time operation but for analyzing a set of captured images of the sight glass. The algorithm requires parameter adjustments based on camera angle and distance, which vary due to different sight glass sizes and camera viewpoints. The implementation processes images from a folder, loading all images numbered sequentially.

This repository serves as a foundation for further development and testing of vision-based refrigerant quality detection systems, providing insights into image processing techniques and algorithmic adjustments necessary for accurate fault detection.
