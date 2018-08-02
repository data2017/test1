# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:10:20 2018

@author: temp
"""
import numpy as np
import cv2 as cv
import random


ColorList = [
   #[127,127,127] , #02
    [  0,  0,  0] ,
    [ 86, 86, 86] ,
    [170,170,170] ,
    [255,255,255] ,
    
    [255,  0,  0] , #03
    [  0,255,  0] , #04
    [  0,  0,255] , #05
    [127,  0,  0] , #06
    [  0,127,  0] , #07
    [  0,  0,127] , #08
    
    [255,255,  0] , # qing se
    [255,  0,255] , # puple
    [  0,255,255] , # yellow
    [127,127,  0] , #
    [120,  0,120] , #
    [  0,127,127] , #
    #[138, 43,226] , #15 puple
]




nRectSize = 32
Image = np.zeros( ( 4*nRectSize , 4*nRectSize , 3 ) )

while True :
    for iColor in range(len(ColorList)) :
        iRow = ( iColor // 4 )
        iCol =   iColor % 4
        pt1 = ( iRow*nRectSize , iCol*nRectSize )
        pt2 = ( iRow*nRectSize + nRectSize-1 , iCol*nRectSize + nRectSize-1 )
    
        #Color = tuple( ColorList[ random.randint( 0, 15 ) ] )
        Color = tuple( ColorList[ iColor ] )
        #print( Color )

        cv.rectangle( Image , pt1 , pt2 , Color , -1 )
    
    #cv.imshow( "Color" , Image )
    #cv.waitKey( 1 )
    cv.imwrite( "I:\\ColorRect.png" , Image )
    break

#hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#HSV空间
#lower_blue=np.array([110,100,100])#blue
#upper_blue=np.array([130,255,255])

#lower_green=np.array([60,100,100])#green
#upper_green=np.array([70,255,255])

#lower_red=np.array([0,100,100])#red
#upper_red=np.array([10,255,255])