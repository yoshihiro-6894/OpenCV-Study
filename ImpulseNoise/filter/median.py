'''
中央値フィルタの実装
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

OrijinalImage = cv2.imread("../Images/Girl.bmp",0)
inputImage = cv2.imread("../noise.jpg",0)
#inputImage = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8,9,10,11],[12,13,14,15]])
cv2.imshow("imput",inputImage)
cv2.imwrite("input.jpg",inputImage)
print(inputImage.shape)

def median_filter(image, kernel, boundary='edge'):
  pad_image = np.pad(image, ((int(kernel[0] / 2),), (int(kernel[1] / 2),)), boundary)
  print(pad_image)
  print("---------------")
  shape = (pad_image.shape[0] - kernel[0] + 1, pad_image.shape[1] - kernel[1] + 1) + kernel
  print(shape)
  strides = pad_image.strides * 2
  strided_image = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel[0] * kernel[1])
  '''
  print( np.lib.stride_tricks.as_strided(pad_image, shape, strides))
  print("-------------")
  print(strided_image)
  '''
  return np.apply_along_axis(lambda a: np.median(a), 2, strided_image)

median_image = median_filter(inputImage,kernel=(5,5))
median_image = median_image.astype(np.uint8)
print(median_image)

cv2.imshow("dst",median_image)
cv2.imwrite("median_output11_11.jpg",median_image)

print(cv2.PSNR(OrijinalImage,inputImage))
print(cv2.PSNR(OrijinalImage,median_image))

cv2.waitKey(0)
cv2.destroyAllWindows()
