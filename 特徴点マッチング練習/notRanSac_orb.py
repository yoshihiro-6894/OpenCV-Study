import cv2

img1 = cv2.imread("./Images/Lenna.bmp",0) # 一枚目
img2 = cv2.imread('./rotate_033.jpg',0) # 二枚目

# Initiate ORB detector
orb = cv2.ORB_create()

# キーポイント検出,ORB記述
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFmatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
# Match descriptors.
matches = bf.match(des1,des2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches,None)

cv2.imshow("img",img3)
cv2.imwrite("notRansac_orb.jpg",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()