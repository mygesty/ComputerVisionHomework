import cv2
import numpy as np
img = cv2.imread("C:\\Users\\THINK\\Pictures\\corner.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)
img_corner = cv2.cornerHarris(img_gray,3,3,0.06)
img_corner = cv2.dilate(img_corner,None)
thred = 0.01*img_corner.max()
img[img_corner>thred] = [255,0,0]
cv2.imshow("corner_point",img)
cv2.waitKey(0)
cv2.destroyAllWindows()