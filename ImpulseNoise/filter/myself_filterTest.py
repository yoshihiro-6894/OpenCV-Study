'''
自作のフィルタを使う(平均値フィルタ)
https://qiita.com/aa_debdeb/items/e74eceb13ad8427b16c6
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

inputImage = cv2.imread("../Images/Lenna.bmp",0)
inputImage = cv2.imread("../noise.jpg",0)

cv2.imshow("imput",inputImage)


print(type(inputImage))
print(inputImage.shape)

def _convolve2d(image, kernel):
  shape = (image.shape[0] - kernel.shape[0] + 1, image.shape[1] - kernel.shape[1] + 1) + kernel.shape
  print(image.shape[0] - kernel.shape[0] + 1, image.shape[1] - kernel.shape[1] + 1)
  strides = image.strides * 2
  strided_image = np.lib.stride_tricks.as_strided(image, shape, strides)
  return np.einsum('kl,ijkl->ij', kernel, strided_image)

def _convolve2d_multichannel(image, kernel):
  convolved_image = np.empty((image.shape[0] - kernel.shape[0] + 1, image.shape[1] - kernel.shape[1] + 1, image.shape[2]))
  for i in range(image.shape[2]):
    convolved_image[:,:,i] = _convolve2d(image[:,:,i], kernel)
  return convolved_image

def _pad_singlechannel_image(image, kernel_shape, boundary):
  return np.pad(image, ((int(kernel_shape[0] / 2),), (int(kernel_shape[1] / 2),)), boundary)

def _pad_multichannel_image(image, kernel_shape, boundary):
  return  np.pad(image, ((int(kernel_shape[0] / 2),), (int(kernel_shape[1] / 2),), (0,)), boundary)

def convolve2d(image, kernel, boundary='edge'):
  if image.ndim == 2:
    pad_image = _pad_singlechannel_image(image, kernel.shape, boundary) if boundary is not None else image
    return _convolve2d(pad_image, kernel)
  elif image.ndim == 3:
    pad_image = _pad_multichannel_image(image, kernel.shape, boundary) if boundary is not None else image
    return _convolve2d_multichannel(pad_image, kernel)


def create_averaging_kernel(size):
  return np.full(size, 1 / (size[0] * size[1]))



averaging3x3_kernel = create_averaging_kernel((3, 3))

outputImage = convolve2d(inputImage,averaging3x3_kernel)
print("outputImage.shape:" + str(outputImage.shape))
outputImage = outputImage.astype(np.uint8)
cv2.imshow("dst",outputImage)
cv2.imwrite("output.jpg",outputImage)

cv2.waitKey(0)
cv2.destroyAllWindows()