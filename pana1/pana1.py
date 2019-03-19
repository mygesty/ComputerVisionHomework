# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:09:57 2018

@author: qzxy
"""

import numpy as np
import cv2

MIN_MATCH_COUNT = 10

def detectAndDecribe(img):
    # 转化为灰度图
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    
    kp, des = sift.detectAndCompute(gray,None)
    return (kp,des)

def matchKeypoints(kp1,kp2,des1,des2,reprojThresh,ratio):
    
    # Initialize SIFT 
	sift = cv2.xfeatures2d.SIFT_create()

	# Extract keypoints and descriptors
	k1, d1 = sift.detectAndCompute(img1, None)
	k2, d2 = sift.detectAndCompute(img2, None)

	# Bruteforce matcher on the descriptors
	bf = cv2.BFMatcher()
	matches = bf.knnMatch(d1,d2, k=2)

	# Make sure that the matches are good
	verified_matches = []
	for m1,m2 in matches:
		# Add to array only if it's a good match
		if m1.distance < reprojThresh * m2.distance:
			verified_matches.append(m1)

	# Mimnum number of matches
	min_matches = 5
	if len(verified_matches) > min_matches:
		
		# Array to store matching points
		img1_pts = []
		img2_pts = []

		# Add matching points to array
		for match in verified_matches:
			img1_pts.append(k1[match.queryIdx].pt)
			img2_pts.append(k2[match.trainIdx].pt)
		img1_pts = np.float32(img1_pts).reshape(-1,1,2)
		img2_pts = np.float32(img2_pts).reshape(-1,1,2)
		
		# Compute homography matrix
		M, _ = cv2.findHomography(img1_pts, img2_pts, cv2.RANSAC, 3.0)
		return M
	else:
		print ('Error: Not enough matches')
		exit()
    
def stitch(img1,img2,ratio,reprojThresh):
    
    kp1, des1 = detectAndDecribe(img1)
    kp2, des2 = detectAndDecribe(img2)
    
    M = matchKeypoints(kp1,kp2,des1,des2,reprojThresh,ratio) 
    if M is None:
        return None
    else:
        H = M
        result = cv2.warpPerspective(img1, H,(img1.shape[1] + 
                                     img2.shape[1], img1.shape[0]))
#        result[0:img2.shape[0]+1, 0:img2.shape[1]] = img2
            
        return result



img1 = cv2.imread("C:\\Users\\THINK\\Pictures\\house1.jpg")
img2 = cv2.imread("C:\\Users\\THINK\\Pictures\\house2.jpg")

img1 = cv2.resize(img1,(0,0),fx = 0.6,fy = 0.6)
img2 = cv2.resize(img2,(0,0),fx = 0.6,fy = 0.6)
#for i in range(2,5):
#    
#    # 读取两张要匹配的图像
#    result = stitch(img1,img2,0.7,5.0)
#    if i==4:
#        break
#    img1 = result
#    img2 = cv2.imread('campus_00'+str(i)+'.jpg')
result = stitch(img1,img2,0.1,0.5)
cv2.imshow('pano',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

    