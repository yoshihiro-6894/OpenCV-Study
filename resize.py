#リサイズする

import cv2

try:
    img = cv2.imread("./Images/Lenna.bmp")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    SCALE1 = 0.5
    SCALE2 = 1.62
    height = img.shape[0]
    width = img.shape[1]
    #print(img.size)
    print(img.shape)
    print(img.shape[0])
    
    
    dst = cv2.resize(img, (int(width*SCALE1), int(height*SCALE1)))
    cv2.imwrite("./resize0.5.jpg",dst)
    cv2.imshow("dst1",dst)
    print(dst.size)
    print(dst.shape)
    
    dst = cv2.resize(img, (int(width*SCALE2), int(height*SCALE2)))
    cv2.imwrite("./resize1.62.jpg",dst)
    cv2.imshow("dst2",dst)
    print(dst.shape)
    
    dst = cv2.resize(img,(400,200))
    cv2.imwrite("./resize400*200.jpg",dst)
    cv2.imshow("dst3",dst)
    print(dst.shape)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))