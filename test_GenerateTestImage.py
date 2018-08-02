import os, shutil
import cv2 as cv
import random
######################################################################    
def GetImage():
    Image = cv.imread( strGlbFile )    
    return Image

def CompareImage( PrevImage , CurrImage ):
    bTwoImageAreDiff = False;
    
def AddRand( Image , iImageCount ):
    ColorList = [ (255,0,0) , (0,255,0) , (0,0,255) , (0,0,0) , (255,255,255) ]
    nRectSize = 4
    for iRow in range( 10 ):
        for iCol in range( 10 ):
            pt1 = ( iRow*nRectSize , iCol*nRectSize )
            pt2 = ( iRow*nRectSize + nRectSize-1 , iCol*nRectSize + nRectSize-1 )
            #Color = ColorList( random.randint( 0, len(ColorList)-1 ) )
            Color = ColorList[ random.randint( 0, 4 ) ]
            cv.rectangle( Image , pt1 , pt2 , Color , -1 )
            
    return Image            
######################################################################    

strSaveFolder = 'I:\\_Project\\DebugSrcFolder\\'
strGlbFile = 'I:\\_Project\\test.jpg'
######################################################################
if os.path.exists( strSaveFolder ) :
    shutil.rmtree( strSaveFolder )    #os.rmdir( strSaveFolder ) must be empty folder
    os.mkdir( strSaveFolder )  
else:
    os.mkdir( strSaveFolder )  
######################################################################
OrgImage = cv.imread( strGlbFile )

iImageCount = 0
iFileCount = 0
while True :
    TempImage = OrgImage
    TempImage = AddRand( TempImage , iImageCount )
    
    nRepeatTime = 5 #random.randint( 1 , 4 )
    for iRepeat in range( nRepeatTime ):
        strSaveFile = strSaveFolder + "%05d.png"%(iFileCount)
        cv.imwrite( strSaveFile , TempImage )

        print( '%s, repeat = %d' % (strSaveFile,iRepeat) )
        iFileCount = iFileCount + 1
        
        
    iImageCount = iImageCount + 1
    if iImageCount > 100 :
        break

print( 'image num = %d' % iImageCount )    
    

