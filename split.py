# カラー画像の各成分の分離

# cv2.splitでカラー画像を赤、緑、青の各成分へ分離
# 各成分が強さを表す
# 白に近いほど成分が強く黒に近いほど弱いことを示す

import cv2

try:
    img = cv2.imread("./Images/Lenna.bmp")
    
    if img is None:
        print("ファイルを読み込めません")
        import sys
        sys.exit()

    cv2.imshow("img",img)
    
    rgb = cv2.split(img)
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    
    cv2.imwrite("b.jpg",blue)
    cv2.imwrite("g.jpg",green)
    cv2.imwrite("r.jpg",red)
    
    cv2.imshow("blue",blue)
    cv2.imshow("green",green)
    cv2.imshow("red",red)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))