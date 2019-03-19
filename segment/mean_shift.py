import numpy as np
import cv2

img = cv2.imread('roster.jpg')
#cv2.imshow("origin",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray",img_gray)

img_clu = cv2.pyrMeanShiftFiltering(img,15,60)
mask = np.zeros((img_clu.shape[0]+2,img_clu.shape[1]+2),np.uint8)
cv2.floodFill(img,mask,(100,100),(np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)),flags = cv2.FLOODFILL_FIXED_RANGE)
#cv2.imwrite('C:\\Users\\THINK\\Pictures\\img_roster.jpg',img_clu)

cv2.imshow('clu',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
