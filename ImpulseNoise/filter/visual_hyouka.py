import cv2
import numpy as np
import GlobalValue as g

def visual_fn_fp(trueNoise, testNoise, strNoiseRatio="10", methodName="name"):
    fn_img = np.zeros(trueNoise.shape)
    fp_img = np.zeros(trueNoise.shape)
    TP=0
    FN=0
    FP=0
    TN=0
    for i in range(trueNoise.shape[0]):
        for j in range(trueNoise.shape[1]):
            if trueNoise[i][j]>0:
                if testNoise[i][j]>0:
                    TP=TP+1
                else:
                    FN=FN+1
                    fn_img[i,j] = 255
            else:
                if testNoise[i][j]>0:
                    FP=FP+1
                    fp_img[i,j] = 255
                else:
                    TN=TN+1

    cv2.imwrite("FN"+strNoiseRatio+methodName+".png", fn_img)
    cv2.imwrite("FP"+strNoiseRatio+methodName+".png", fp_img)