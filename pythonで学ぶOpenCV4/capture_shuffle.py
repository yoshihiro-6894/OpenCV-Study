# 接続されているカメラから映像を取り出しシャッフルするプログラム

import cv2
import numpy as np

try:
    capture = cv2.VideoCapture(0)
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    roi_target = [0, 1, 2, 3]
    counter = 60
    
    while(True):
        ret, frame = capture.read()
        if ret == False:
            print('カメラから映像を取得できませんでした。')
            break
       
        dst = np.zeros((height, width , 3), np.uint8)
        
        y1 = [0, height//2, height//2, 0]
        y2 = [height//2, height, height, height//2]
        x1 = [0, 0, width//2, width//2]
        x2 = [width//2, width//2, width, width]
        
        for i in range(0, 4):
            dst[y1[i]:y2[i], x1[i]:x2[i]] = \
                frame[y1[roi_target[i]]:y2[roi_target[i]],
                      x1[roi_target[i]]:x2[roi_target[i]]]
                
        counter -= 1
        if counter <= 0:
            counter = 60
            for i in range(0,4):
                roi_target[i] += 1
                if roi_target[i] == 4:
                    roi_target[i] = 0
                
                    
        cv2.imshow("f",dst)
        
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