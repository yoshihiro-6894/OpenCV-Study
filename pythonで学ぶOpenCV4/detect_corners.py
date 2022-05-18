# 画像に含まれるコーナーを検出するプログラム

import cv2
import numpy as np

try:
    MAX_CORNERS = 50
    BLOCK_SIZE = 3
    QUALITY_LEVEL = 0.01
    MIN_DISTANCE = 20.0
    
    img = cv2.imread("./Images/Lenna.bmp")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, MAX_CORNERS, QUALITY_LEVEL,
                                      MIN_DISTANCE, blockSize = BLOCK_SIZE,
                                      useHarrisDetector = False)
    
    print(corners)
    
    for i in corners:
        x,y = i.ravel()
        print(i)
        x = x.astype(int)
        y = y.astype(int)
        cv2.circle(img, (x,y), 4, (255,255,0), 2)
        
    cv2.imwrite("corners.jpg",img)
    cv2.imshow("img",img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))