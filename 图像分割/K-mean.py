import numpy as np
import cv2

img = cv2.imread('roster.jpg')
cv2.imshow("origin",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img_gray)
Z = img.reshape((-1,3))
Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
_,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
img_clu = res.reshape((img.shape))


cv2.imshow('clu',img_clu)
cv2.waitKey(0)
cv2.destroyAllWindows()