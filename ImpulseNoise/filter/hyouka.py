import cv2
import numpy as np
import GlobalValue as g

def hyou(trueNoise, testNoise):
    print("hyouka")
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
            else:
                if testNoise[i][j]>0:
                    FP=FP+1
                else:
                    TN=TN+1


    print("TP"+str(TP)+" "+"FN"+str(FN)+ " "+"FP"+str(FP)+" "+"TN"+str(TN))

    if TP ==0:
        print("TPが0のため略")
        return

    Precision=TP/(TP+FP)
    recall=TP/(TP+FN)
    print("適合率:"+str(Precision)+"再現率:"+str(recall))

    F=(2*Precision*recall)/(Precision+recall)
    print("F値:"+str(F))

    return str(format(F, '.3f'))


def Update_imgBinary(baseBinary, addBinary):
    updateBinary = baseBinary.copy()
    for i in range(baseBinary.shape[0]):
        for j in range(baseBinary.shape[1]):
            if baseBinary[i,j]>0 or addBinary[i,j]>0:
                updateBinary[i,j] = 1
            else:
                updateBinary[i,j] = 0

    return updateBinary
