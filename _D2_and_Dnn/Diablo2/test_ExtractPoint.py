# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:13:35 2017

@author: temp
"""
import os, sys
from PIL import ImageGrab
import cv2
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt


def TestImgGrab():
       ## get win rect and move to top-left position
    hWnd =win32gui.FindWindow(0, 'D2Loader v1.11b - Build On Nov 11 2005' )
    rect = win32gui.GetWindowRect( hWnd )
    
    for i in range(1000):
        img = ImageGrab.grab( rect )
        
        opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

        cv2.imshow( "test" ,  opencvImage )
        cv2.waitKey( 1 )
        time.sleep( 1 )
        
        
strFile = 'D:\Games\d2_jpg\DetectPoint\DetectPoint_1.jpg'
ImgOrg  = cv2.imread( strFile )
ImgGray = cv2.cvtColor( ImgOrg , cv2.COLOR_BGR2GRAY )

cv2.imshow( "ImgOrg" , ImgOrg )

##      square, circle, 
## dark
## whit
## R    enymy
## G    ally
## B  


[Bb,Gg,Rr] = cv2.split( ImgOrg ) #split -- merge
ImgGrayInRgb = cv2.merge( [ ImgGray , ImgGray , ImgGray ] )
cv2.imshow( "Bb" , Bb )
cv2.imshow( "Gg" , Gg )
cv2.imshow( "Rr" , Rr )


ImgRed = ImgOrg;
ImgRed[:,:,0] = 0;
ImgRed[:,:,1] = 0;
#ImgRed[:,:,2] = 0;
#emptyImage2 = img.copy()  
  
#emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  

#kernel = np.ones((5,5),np.float32)/25
#nRadius = 3;
#nRadius = 5;  nConvTh = 200;
nRadius = 3;  nConvTh = 244;
kernel = np.ones((nRadius,nRadius),np.float32)/(nRadius*nRadius)
dst = cv2.filter2D( Rr , -1 , kernel )
#Pos = np.where( dst >= np.max(dst)-5 )
Pos = np.where( dst >= nConvTh )
#cv2.imshow( "Rr" , Rr )

for iPoint in range(Pos[0].size) :
    print( Pos[0][iPoint] , Pos[1][iPoint] )
    center = (  Pos[1][iPoint]  , Pos[0][iPoint] )
    color  = ( 255 , 0 , 0 )
    cv2.circle( ImgGrayInRgb , center, 2 , color , 2 )
cv2.imshow( "ImgGrayInRgb" , ImgGrayInRgb )
    
    
OneRow = dst.reshape( -1 )
#plt.hist( OneRow , 255 )



cv2.waitKey ( 0 )  
sys.exit() #os._exit()

cv2.imshow( "conv" , dst )

#cv2.imshow("Org" , ImgOrg )  
#cv2.imshow("Gray", ImgGray)  
#cv2.imshow("Bb" , Bb )
#cv2.imshow("Gg" , Gg )
#cv2.imshow("Rr" , Rr )
#cv2.imshow("RedOnly" , ImgRed )  


cv2.waitKey ( 0 )  
#cv2.destroyAllWindows()  





