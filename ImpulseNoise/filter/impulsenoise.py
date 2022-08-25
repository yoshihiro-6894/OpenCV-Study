'''
https://qiita.com/bohemian916/items/9630661cd5292240f8c7
'''

import cv2
import os
import glob
import numpy as np

def addNoise(img, amount):
  row,col = img.shape
  No_amount = 0.02 * amount
  sp_img = img.copy()
  binary_noise = np.zeros(sp_img.shape)
  count=0

  num_salt = np.ceil(No_amount * img.size)
  print(int(num_salt))
  print(No_amount/2 * img.size)
  coords = [np.random.randint(0, i-1 , int(num_salt)) for i in img.shape]
  coord= np.array(coords)
  #print(coord.shape)
  for i in range(coord.shape[1]):
      if(i%2==0):
          sp_img[coord[1][i]][coord[0][i]]=255
      else:
          sp_img[coord[1][i]][coord[0][i]]=0
      binary_noise[coord[1][i]][coord[0][i]]=255
      
  for i in range(sp_img.shape[1]):
    for j in range(sp_img.shape[0]):
      if (binary_noise[j][i]==255):
        count = count+1
  print(count)
  print("\n\n")
  cv2.imwrite("noiseBinary"+str(int(amount))+"%.png",binary_noise)
  return sp_img



os.chdir("testDir")

str_imgs=glob.glob('*.png')

for i in range(len(str_imgs)):
  print(str_imgs[i]+"を読み込みました")
  input_img=cv2.imread(str_imgs[i],0)
  dirTex="0"+str(i+1)+"n"
  if os.path.exists(dirTex) != True:
    os.mkdir(dirTex)
    print("作成:"+dirTex)
  os.chdir(dirTex)

  for j in range(9):
    noise=addNoise(input_img,(j+1)*10)
    cv2.imwrite("Noise"+str((j+1)*10)+"%.png",noise)
  os.chdir("..")
  


'''
cv2.imshow("test",image)


for i in range(9):
  cv2.imshow("noise"+str(i),addNoise(image,(i+1)*10))

print(glob.glob('*.png'))
'''

cv2.waitKey(0)
cv2.destroyAllWindows()