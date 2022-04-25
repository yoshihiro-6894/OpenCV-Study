import cv2
import numpy as np

try:
    img = cv2.imread("./Images/Lenna.bmp")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()
        
    rows, cols = img.shape[:2]
    print(rows,cols)
    
    x0 = cols/4
    x1 = (cols*3)/4
    y0 = rows/4
    y1 = (rows*3)/4
    
    #[左上],[左下],[右下],[右上]
    list_src = np.float32([[x0, y0], [x0, y1], [x1, y1], [x1, y0]])
    print("list_src")
    print(list_src)
    
    #pattern-0
    print("pattern-0")
    x_margin = cols/10
    y_margin = rows/10
    list_dsts = np.float32([[x0+x_margin,y0+y_margin],list_src[1],list_src[2],
                           [x1-x_margin,y0+y_margin]])
    print("list_dsts")
    print(list_dsts)
    
    perspective_matrix = cv2.getPerspectiveTransform(list_src,list_dsts)
    dst = cv2.warpPerspective(img, perspective_matrix, (cols,rows))
    
    cv2.imwrite("./dest0.jpg",dst)
    cv2.imshow("dst0",dst)
    
    
    #pattern-1
    print("pattern-1")
    x_margin = cols/8
    y_margin = rows/8
    list_dsts = np.float32([list_src[0],list_src[1],
                           [x1-x_margin, y1-y_margin],
                           [x1-x_margin, y0+y_margin]])
    print("list_dsts")
    print(list_dsts)
    
    perspective_matrix = cv2.getPerspectiveTransform(list_src,list_dsts)
    dst = cv2.warpPerspective(img, perspective_matrix, (cols,rows))
    
    cv2.imwrite("./dest1.jpg",dst)
    cv2.imshow("dst1",dst)
    
    #pattern-2
    print("pattern-2")
    x_margin = cols/6
    y_margin = rows/6
    list_dsts = np.float32([[x0+x_margin, y0+y_margin],list_src[1],
                           [x1-x_margin, y1-y_margin],list_src[3]])
    
    print("list_dsts")
    print(list_dsts)
    
    perspective_matrix = cv2.getPerspectiveTransform(list_src,list_dsts)
    dst = cv2.warpPerspective(img, perspective_matrix, (cols,rows))
    
    cv2.imwrite("./dest2.jpg",dst)
    cv2.imshow("dst2",dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))