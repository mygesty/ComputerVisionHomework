import cv2
import numpy as np

img = cv2.imread("C:\\Users\\THINK\\Pictures\\beauty2.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(img_gray,0.05*img_gray.max(),255,0)
image,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img_gray,contours,-1,(255,0,0),2)
cv2.imshow("contours",img)
cv2.waitKey()
cv2.destroyAllWindows()