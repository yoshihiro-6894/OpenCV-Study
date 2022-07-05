'''
https://qiita.com/bohemian916/items/9630661cd5292240f8c7
'''

import cv2
import numpy as np

img = cv2.imread("./Images/Girl.bmp",1)
row,col,ch = img.shape

print(row,col,ch)

print(img.size)
s_vs_p = 0.5
amount = 0.1
sp_img = img.copy()

# 塩モード
num_salt = np.ceil(amount * img.size * s_vs_p)
coords = [np.random.randint(0, i-1 , int(num_salt)) for i in img.shape]
sp_img[coords[:-1]] = (255,255,255)

# 胡椒モード
num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
coords = [np.random.randint(0, i-1 , int(num_pepper)) for i in img.shape]
sp_img[coords[:-1]] = (0,0,0)

cv2.imshow("dst",sp_img)
cv2.imwrite("noise.jpg",sp_img)

cv2.waitKey(0)
cv2.destroyAllWindows()