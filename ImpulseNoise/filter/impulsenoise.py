'''
https://qiita.com/bohemian916/items/9630661cd5292240f8c7
'''

import cv2
import os
import glob
import numpy as np

def addNoise(img, amount):
  row,col = img.shape
  No_amount = 0.01 * amount
  sp_img = img.copy()
  binary_noise = np.zeros(sp_img.shape)
  count=0

  num_salt = np.ceil(5 * No_amount * img.size)
  print(int(num_salt))
  mokuhyou = int(np.ceil(No_amount * img.size))
  print("目標ノイズ個数"+str(np.ceil(No_amount * img.size)))
  #print(mokuhyou)
  coordsy = [np.random.randint(0, row , int(num_salt))]
  coordsx = [np.random.randint(0, col , int(num_salt)) ]
  coordy = np.array(coordsy)
  coordx = np.array(coordsx)

  '''
  coords = np.stack(coordx,coordy,0)
  print(corrds.shape[0])
  '''

  for i in range(coordx.shape[1]):
    if binary_noise[coordy[0][i]][coordx[0][i]]==0:
      sp_img[coordy[0][i]][coordx[0][i]]=np.random.randint(0,256)
      '''
      if(i%2==0):
          sp_img[coordy[0][i]][coordx[0][i]]=np.random.randint(128,256)
      else:
          sp_img[coordy[0][i]][coordx[0][i]]=np.random.randint(0,128)
      '''
      binary_noise[coordy[0][i]][coordx[0][i]]=255
      count=count+1
    
    if count>=mokuhyou:
      print("owari")
      break
      
  count=0
  for i in range(sp_img.shape[1]):
    for j in range(sp_img.shape[0]):
      if (binary_noise[j][i]==255):
        count = count+1
  print("付与したノイズ個数:"+str(count)+"\n")
  cv2.imwrite("noiseBinary"+str(int(amount))+"%.png",binary_noise)
  return sp_img

#os.chdir("randomNoise/BSD68")
os.chdir("randomNoise/Set12")

str_imgs=glob.glob('*.png')

for i in range(len(str_imgs)):
  print(str_imgs[i]+"を読み込みました")
  dirTex="0"+str(i+1)+"n"
  if os.path.exists(dirTex) != True:
    os.mkdir(dirTex)
    print("作成:"+dirTex)
  os.chdir(dirTex)
  #cv2.imwrite("orijinal.png",input_img)
  
  input_img=cv2.imread("orijinal.png",0)
  print(input_img.shape)
  for j in range(9):
    noise=addNoise(input_img,(j+1)*10)
    cv2.imwrite("Noise"+str((j+1)*10)+"%.png",noise)
  os.chdir("..")
  print("\n")


'''
cv2.imshow("test",image)


for i in range(9):
  cv2.imshow("noise"+str(i),addNoise(image,(i+1)*10))

print(glob.glob('*.png'))
'''

cv2.waitKey(0)
cv2.destroyAllWindows()