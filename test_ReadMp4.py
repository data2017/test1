import cv2  
import numpy

#cap = cv2.VideoCapture("I:\_Project\RandImage\VID_20180325_204303.mp4")
cap = cv2.VideoCapture("I:\_Project\RandImage\VID_20180325_215149.mp4")

iCount = 0
while(1):
    
    # get a frame
    ret, frame = cap.read()
    iCount = iCount + 1
    
    print( iCount )
    if iCount < 30*30 : 
        continue;
        
    # show a frame
    if 1 :
        cv2.imshow("capture", frame)
        if cv2.waitKey(1111) & 0xFF == ord('q'):
            break
    else:
        cv2.imwrite( "I:\_Project\RandImage\DebugImg\%08d.png"%(iCount) , frame)        
