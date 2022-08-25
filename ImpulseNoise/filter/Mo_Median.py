'''
普通の中央値フィルタ
'''


import numpy as np
import cv2

def median_filter(image, kernel, boundary='reflect'):
    print("普通の中央値フィルタ")
    pad_image = np.pad(image, ((int(kernel.shape[0] / 2),), (int(kernel.shape[1] / 2),)), boundary)
    shape = (pad_image.shape[0] - kernel.shape[0] + 1, pad_image.shape[1] - kernel.shape[1] + 1) + kernel.shape
    strides = pad_image.strides * 2
    # as_strided()でpad_imageをshapeの大きさの配列をスライドしたような配列を生成する
    strided_image = np.lib.stride_tricks.as_strided(pad_image, shape, strides).reshape(shape[0], shape[1], kernel.shape[0] * kernel.shape[1])
    #print(strided_image)
    return np.apply_along_axis(lambda a: np.median(a),2,strided_image)