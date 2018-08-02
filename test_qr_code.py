#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:05:51 2018

@author: nvidia
"""
#import cv2 as cv
import qrcode  #pip install qrcode
#import zbar    
#import zxing
import zbarlight as zl # zl = import zbarlight

qr = qrcode.QRCode( 
        version=1 ,
        error_correction=qrcode.constants.ERROR_CORRECT_L,  #L,M,Q,H=7,15,25,30
        box_size=4 , 
        border=8 )

qr.add_data( "0123456789"*222*2 )

qr.make( fit=True )

img = qr.make_image()
#img.show()
print( 'img is mde\n' )

codes = zl.scan_codes( 'qrcode' , img )
print( codes )

#cv.imshow( img )
#cv.waitKey( )
