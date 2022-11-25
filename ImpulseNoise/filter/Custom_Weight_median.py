'''
重み付きフィルタの実装
'''


import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import os

# 自作モジュール
import GlobalValue as g
import Mo_Median
import Mo_simple
import custom1
import custom2
import custom2_1
import custom_mean
import custom_next

# 自作randomNoiseFilterモジュール
import custom_random1
import Loop_random1
import custom_random_rowcol
import custom_tripleThreshold
import visual_hyouka


def W(image):
  global count
  sort_R = np.sort(image)
  diff_D = np.diff(sort_R)
  argsort = np.argsort(diff_D)
  maxs = argsort[-4:]
  p = np.min(maxs)
  t = np.max(maxs)
  w_min = sort_R[p+1]
  w_max = sort_R[t]
  forcus = image[math.floor(len(image)/2)]
  if (forcus<w_min) or (w_max<forcus):
    count= count+1
    return np.median(sort_R)
  else:
    return forcus
  print(maxs)
  print(len(image))
  print(math.ceil(len(image)/2))

  return np.median(sort_R)


def median_filter(image, kernel, boundary='reflect'):
  pad_image = np.pad(image, ((int(kernel.shape[0] / 2),), (int(kernel.shape[1] / 2),)), boundary)
  shape = (pad_image.shape[0] - kernel.shape[0] + 1, pad_image.shape[1] - kernel.shape[1] + 1) + kernel.shape
  strides = pad_image.strides * 2
  print(pad_image.shape)
  print("------------------")
  # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
  strided_image = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel.shape[0] * kernel.shape[1])
  #print(strided_image)
  return np.apply_along_axis(lambda a: W(a),2,strided_image)
  return np.apply_along_axis(lambda a: np.median(a), 2, strided_image)

g.count=0
firsttext="01"
dirtext="./randomNoise/Set12/"
NoiseRatio="40"

#OrijinalImage = cv2.imread("../Images/Set12/"+firsttext+".png",0)
OrijinalImage = cv2.imread(dirtext+firsttext+"n/orijinal.png",0)
#cv2.imshow("orijinal",OrijinalImage)

inputImage = cv2.imread(dirtext+firsttext+"n/Noise"+NoiseRatio+"%.png",0)
g.TruenoiseBinary = cv2.imread(dirtext+firsttext+"n/noiseBinary"+NoiseRatio+"%.png",0)
g.img_binary = g.TruenoiseBinary.copy()
#inputImage = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8,9,10,11],[12,13,14,15]])
W_kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])
as_strided_W_kernel = np.lib.stride_tricks.as_strided(W_kernel, shape=(W_kernel.shape[0] * W_kernel.shape[1],))
cv2.imshow("imput",inputImage)
cv2.imwrite("noise.png",inputImage)
print("PSNR:"+str(cv2.PSNR(OrijinalImage,inputImage)))


'''
フィルタをかける
'''
print("フィルタ処理")
print("ノイズ割合"+str(NoiseRatio))

os.chdir(dirtext+firsttext+"n")

median_image = Mo_Median.median_filter(inputImage, kernel=W_kernel)
median_image = median_image.astype(np.uint8)
print("PSNR:"+str(cv2.PSNR(OrijinalImage, median_image)))
cv2.imshow("dst1",median_image)
cv2.imwrite("median_output.png",median_image)

'''
median_image = cv2.medianBlur(inputImage,3)
print("PSNR:"+str(cv2.PSNR(OrijinalImage, median_image)))
cv2.imshow("median",median_image)
'''

''' simple検出
median_image = Mo_simple.median_filter(inputImage,kernel=np.zeros([11,11]))
median_image = median_image.astype(np.uint8)
print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
cv2.imshow("dst2",median_image)
cv2.imwrite("simple_median_output.png",median_image)
print("count="+str(g.count))
g.count=0
'''


#custom1_random1
median_image = custom_random1.median_filter(inputImage)
median_image = median_image.astype(np.uint8)
print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
cv2.imshow("dst3",median_image)
cv2.imwrite("custom1_median_output"+NoiseRatio+".png",median_image)
visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=NoiseRatio,methodName="custom1")

'''
print("\nLoop\n")
Loop_random1.loop_custom(inputImage)
'''

median_image = custom_random_rowcol.median_filter(inputImage,size=5)
median_image = median_image.astype(np.uint8)
print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
cv2.imshow("dst_rowcol",median_image)
cv2.imwrite("custom_random_rowcol"+NoiseRatio+".png",median_image)
visual_hyouka.visual_fn_fp(g.TruenoiseBinary,g.img_binary,strNoiseRatio=NoiseRatio,methodName="rowcol")


#custom_tripleThreshold.filter(inputImage)

'''絶対消すな
g.count=0
median_image = custom2.mean_filter(inputImage)
median_image = median_image.astype(np.uint8)
print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
cv2.imshow("dst4",median_image)
cv2.imwrite("custom2_median_output.png",median_image)

g.count=0
median_image = custom2_1.mean_filter(inputImage)
median_image = median_image.astype(np.uint8)
print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
cv2.imshow("dst5",median_image)

cv2.imwrite("custom2_1_median_output.png",median_image)

g.count=0
median_image = custom_next.mean_filter(inputImage)
median_image = median_image.astype(np.uint8)
cv2.imshow("mean_1",median_image)
#median_image = custom_next.mean_filter(median_image)
#median_image = median_image.astype(np.uint8)
median_image = custom2.mean_filter(median_image)
median_image = median_image.astype(np.uint8)
print("PSNR:"+str(cv2.PSNR(OrijinalImage,median_image)))
cv2.imshow("mean",median_image)
cv2.imwrite("custom_mean_output.png",median_image)

#median_image = median_filter(inputImage,kernel=W_kernel)
#median_image = median_filter(median_image,kernel=W_kernel)

#print(median_image)
print("count="+str(g.count))
'''
print("\nPlease enter any key\n")
cv2.waitKey(0)
cv2.destroyAllWindows()
