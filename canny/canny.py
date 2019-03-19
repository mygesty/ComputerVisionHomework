# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:16:09 2018

@author: THINK
"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\THINK\\Pictures\\beauty3.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_gray = cv2.GaussianBlur(img_gray,(5,5),0)

img_canny1_1 = cv2.Canny(img_gray,30,20)
img_canny1_2 = cv2.Canny(img_gray,30,11)
img_canny1_3 = cv2.Canny(img_gray,30,7.5)
img_canny1 = np.hstack((img_canny1_1,img_canny1_2,img_canny1_3))
cv2.imshow("mybeauty1",img_canny1)


img_canny2_1 = cv2.Canny(img_gray,75,50)
img_canny2_2 = cv2.Canny(img_gray,75,27)
img_canny2_3 = cv2.Canny(img_gray,75,18)
img_canny2 = np.hstack((img_canny2_1,img_canny2_2,img_canny2_3))
cv2.imshow("mybeauty2",img_canny2)


img_canny3_1 = cv2.Canny(img_gray,125,83)
img_canny3_2 = cv2.Canny(img_gray,125,45)
img_canny3_3 = cv2.Canny(img_gray,125,31)
img_canny3 = np.hstack((img_canny3_1,img_canny3_2,img_canny3_3))
cv2.imshow("mybeauty3",img_canny3)


img_canny4_1 = cv2.Canny(img_gray,175,116)
img_canny4_2 = cv2.Canny(img_gray,175,63)
img_canny4_3 = cv2.Canny(img_gray,175,43)
img_canny4 = np.hstack((img_canny4_1,img_canny4_2,img_canny4_3))
cv2.imshow("mybeauty4",img_canny4)

img_canny5_1 = cv2.Canny(img_gray,225,150)
img_canny5_2 = cv2.Canny(img_gray,225,81)
img_canny5_3 = cv2.Canny(img_gray,225,56)
img_canny5 = np.hstack((img_canny5_1,img_canny5_2,img_canny5_3))
cv2.imshow("mybeauty5",img_canny5)

cv2.imshow('beauty',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
