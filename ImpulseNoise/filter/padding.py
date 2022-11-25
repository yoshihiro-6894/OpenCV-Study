import numpy as np

def pad_stride_reshape(image,kernel,boundary="reflect"):
  pad_image = np.pad(image, ((int(kernel.shape[0] / 2),), (int(kernel.shape[1] / 2),)), boundary)
  shape = (pad_image.shape[0] - kernel.shape[0] + 1, pad_image.shape[1] - kernel.shape[1] + 1) + kernel.shape
  strides = pad_image.strides * 2
  # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
  # 下と違い、reshapeをする
  return np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel.shape[0] * kernel.shape[1])

def pad_stride(image,kernel,boundary="reflect"):
  pad_image = np.pad(image, ((int(kernel.shape[0] / 2),), (int(kernel.shape[1] / 2),)), boundary)
  shape = (pad_image.shape[0] - kernel.shape[0] + 1, pad_image.shape[1] - kernel.shape[1] + 1) + kernel.shape
  strides = pad_image.strides * 2
  # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
  # 上と違い、reshapeしない
  return np.lib.stride_tricks.as_strided(pad_image, shape, strides)