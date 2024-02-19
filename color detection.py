#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


# Define the lower and upper bounds for each color (in HSV color space)
color_ranges = {
    'red': [(0, 100, 100), (10, 255, 255)],
    'green': [(35, 100, 100), (85, 255, 255)],
    'blue': [(100, 100, 100), (140, 255, 255)],
    'yellow': [(20, 100, 100), (30, 255, 255)],
    'orange': [(10, 100, 100), (25, 255, 255)],
}


# In[3]:


# Function to detect a specific color in a frame
def detect_color(frame, color_name, lower, upper):
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Create a mask to extract the color from the frame
    mask = cv2.inRange(hsv_frame, lower, upper)
     # Apply a series of morphological operations to clean up the mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a bounding box around the detected color region
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color_map[color_name], 2)



# In[4]:


# Define colors and corresponding BGR values
color_map = {
    'red': (0, 0, 255),
    'green': (0, 255, 0),
    'blue': (255, 0, 0),
    'yellow': (0, 255, 255),
    'orange': (0, 165, 255),
}


# In[5]:


# Capture video from the webcam (change 0 to the video file path if using a file)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect and display each specified color
    for color_name, (lower, upper) in color_ranges.items():
        detect_color(frame, color_name, np.array(lower), np.array(upper))

    # Display the original frame with detected colors
    cv2.imshow('Color Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




