import cv2
import numpy as np
import GlobalValue as g

def hyou(trueNoise, testNoise):
    TP=0
    FN=0
    FP=0
    TN=0
    for i in range(trueNoise.shape[0]):
        for j in range(trueNoise.shape[1]):
            if trueNoise[j][i]>0:
                if testNoise[j][i]>0:
                    TP=TP+1
                else:
                    FN=FN+1
            else:
                if testNoise[j][i]>0:
                    FP=FP+1
                else:
                    TN=TN+1


    print("TP"+str(TP))
    print("FN"+str(FN))
    print("FP"+str(FP))
    print("TN"+str(TN))

    if TP ==0:
        print("TPが0のため略")
        return

    Precision=TP/(TP+FP)
    print("適合率:"+str(Precision))

    recall=TP/(TP+FN)
    print("再現率:"+str(recall))

    F=(2*Precision*recall)/(Precision+recall)
    print("F値:"+str(F))