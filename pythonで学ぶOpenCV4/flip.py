#フリップさせる(反転)
import cv2

try:
    img = cv2.imread('./Images/Lenna.bmp')
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    #flip(src,filecode)
    #src -> 入力画像(配列)
    #filecode -> フリップの方向
        #  0 -> x軸周りでの反転(上下反転)
        # >0 -> y軸周りでの反転(左右反転)
        # <0 -> 両軸周りでの反転
    
    #上下反転
    dst = cv2.flip(img,0)
    cv2.imwrite("./flip0.jpg",dst)
    cv2.imshow("dst1",dst)
    
    #左右反転
    dst = cv2.flip(img,1)
    cv2.imwrite("./flip1.jpg",dst)
    cv2.imshow("dst2",dst)
    
    #両軸反転
    dst = cv2.flip(img,-1)
    cv2.imwrite("./flip2.jpg",dst)
    cv2.imshow("dst3",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))