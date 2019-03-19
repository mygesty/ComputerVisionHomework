import cv2

img = cv2.imread("C:\\Users\\THINK\\Pictures\\varese.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img_gray = (img_gray*1.6).astype(np.uint8)


sift = cv2.xfeatures2d.SIFT_create(800)
keypoints,descriptor = sift.detectAndCompute(img_gray,None)
img = cv2.drawKeypoints(img,keypoints,img,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



cv2.imshow("sift_feature",img)
cv2.waitKey()
cv2.destroyAllWindows()