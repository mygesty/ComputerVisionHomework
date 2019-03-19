# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:54:06 2018

@author: THINK
"""

import cv2
import numpy as np


img = cv2.imread('C:\\Users\\THINK\\Pictures\\bicycle.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray,125,83)
im_canny = cv2.GaussianBlur(img_canny,(5,5),0)
Lines = cv2.HoughLinesP(img_canny,1,1*np.pi/180,80,80,10)
circles = cv2.HoughCircles(img_canny,cv2.HOUGH_GRADIENT,1,200,200,100)
for i in range(len(circles[0])):
    cv2.circle(img,((circles[0][i])[0],(circles[0][i])[1]),(circles[0][i])[2],(0,0,255),10)
for i in range(len(Lines)):
    cv2.line(img,((Lines[i])[0][0],(Lines[i])[0][1]),((Lines[i])[0][2],(Lines[i])[0][3]),(0,255,0),9)
cv2.imshow('lines',img_canny)
cv2.imshow('bicycle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

