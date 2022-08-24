'''
https://qiita.com/bohemian916/items/9630661cd5292240f8c7
'''

import cv2
import numpy as np

img = cv2.imread("./Lenna.jpg",0)
row,col = img.shape

print(row,col)

print(img.size)
amount = 0.1
sp_img = img.copy()

num_salt = np.ceil(amount * img.size)
coords = [np.random.randint(0, i-1 , int(num_salt)) for i in img.shape]
coord= np.array(coords)
for i in range(coord.shape[1]):
    if(i%2==0):
        sp_img[coord[1][i]][coord[0][i]]=255
    else:
        sp_img[coord[1][i]][coord[0][i]]=0

cv2.imshow("dst",sp_img)
#cv2.imwrite("noise.jpg",sp_img)

cv2.waitKey(0)
cv2.destroyAllWindows()