import cv2

try:
    src1 = cv2.imread("./Images/Lenna.bmp")
    src2 = cv2.imread("./rotate_033.jpg")
    
    if src1 is None or src2 is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
    
    detector = cv2.AKAZE_create()
    keypoints1, descriptor1 = detector.detectAndCompute(src1, None)
    keypoints2, descriptor2 = detector.detectAndCompute(src2, None)
    
    '''
    cv2.BFMatcher: 総当りによるマッチング (Brute Force Matching) を行う。
    cv2.FlannBasedMatcher 近似近傍探索手法 Flann によるマッチングを行う。
    '''
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = matcher.match(descriptor1,descriptor2)
    dst = cv2.drawMatches(src1, keypoints1, src2, keypoints2, matches, None,
                          flags = 2)
    
    key = detector.detect(src1)
    out = cv2.drawKeypoints(src1, key, None)
    cv2.imshow("out",out)
    
    cv2.imwrite("akaze.jpg",dst)
    cv2.imshow("dst",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))