# ブラー処理(平滑化)
# 指定したカーネルサイズで平滑化を行う
# サイズ領域の中央値を用いる

import cv2

try:
    img = cv2.imread("./Images/Lenna.bmp")
    #img = cv2.imread("./Images/Lenna.bmp",cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    cv2.imshow("img",img)
    
    #cv2.medianBlur(img,ksize)
    #ksize -> ブラー処理に使用するカーネルサイズ、中央値を採用するため絶対に奇数にすること
    
    dst = cv2.medianBlur(img,11)
    cv2.imwrite("medianBlur1.jpg",dst)
    cv2.imshow("dst1",dst)
    
    dst = cv2.medianBlur(img,33)
    cv2.imwrite("medianBlur2.jpg",dst)
    cv2.imshow("dst2",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))