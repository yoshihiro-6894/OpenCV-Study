# 適応的閾値処理(アダプチィブスレッショルド処理)

import cv2

try:
    img = cv2.imread("./Images/Lenna.bmp",cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    cv2.imshow("img",img)

    #cv2.adaptiveThreshold(src,maxval,adaptiveMethod,thresholdType,
    #                        blockSize,C)
    #src -> 入力配列(画像)
    #maxval -> thresholdTypeで用いられる最大値
    #adaptiveMethod -> 適応的閾値アルゴリズム MEAN_C,GAUSSIAN_Cがある
    #thresholdType -> BINARY,BINARY_INVがある
    #blockSize -> 閾値を算出するために使用する近傍領域のサイズ
    #C -> 平均または加重平均から減産される定数
    
    dst = cv2.adaptiveThreshold(img,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY,7,8)
    cv2.imwrite("./adaptiveThreshold.jpg",dst)
    cv2.imshow("dst",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))