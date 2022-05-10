# 接続されているカメラから映像を取り出し一部分だけ回転させるプログラム

import cv2

try:
    capture = cv2.VideoCapture(0)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    center = (width//4, height//4)
    degree = 0.0
    roi = [width//4, height//4, (width*3)//4, (height*3)//4]
    
    while(True):
        ret, frame = capture.read()
        if ret == False:
            print('カメラから映像を取得できませんでした。')
            break
        
        frame_part = frame[roi[1]:roi[3], roi[0]:roi[2]]
        
        affin_trans = cv2.getRotationMatrix2D(center, degree, 1.0)
        dst = cv2.warpAffine(frame_part, affin_trans, (width//2,height//2),
                             flags = cv2.INTER_CUBIC)
        degree += 1.0
        frame[roi[1]:roi[3], roi[0]:roi[2]] = dst
                    
        cv2.imshow("f",frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    capture.release()
    cv2.destroyAllWindows()
except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))