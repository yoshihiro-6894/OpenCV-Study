# 画像に含まれるコーナーを検出するプログラム

import cv2
import numpy as np

try:
    MAX_CORNERS = 50
    BLOCK_SIZE = 3
    QUALITY_LEVEL = 0.01
    MIN_DISTANCE = 20.0
    
    img = cv2.imread("./Images/Lenna.bmp")
    img = cv2.imread("./D-Textureless/train/model_03.png")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    gray = np.float32(gray)
    gray1 = cv2.medianBlur(gray, 3)
    k = 1.0
    kernel = np.array([[-k, -k, -k], [-k, 1+8*k, -k], [-k, -k, -k]])
    gray2 = cv2.filter2D(gray1, ddepth=-1, kernel=kernel)
    dst = cv2.cornerHarris(gray2,2,3,0.00)
    
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
        
    cv2.imwrite("corners_textureless.jpg",img)
    cv2.imshow("img",img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))