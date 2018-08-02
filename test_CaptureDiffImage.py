import os, shutil
#import VideoCapture

import cv2 as cv
iGlbFile = 0
capture=cv.VideoCapture(0)
print( 'capture is opend = ' , end = '' )
print( capture.isOpened() )

######################################################################    
def GetImage():
    
    global iGlbFile
    global strReadFolder
    strReadFile = strReadFolder + '%05d.png' % iGlbFile
    #Image = cv.imread( strReadFile )    
    
    ret,img=capture.read()
    Image = img
    print( ret )
    iGlbFile = iGlbFile + 1
    
    print( "######### %s" % (strReadFile) )
    #print( Image.shape )

    return Image
    
def ImageIsEqual( PrevImage , CurrImage ):
    bIsEqual = ( PrevImage == CurrImage ).all()
    return bIsEqual

######################################################################    
strReadFolder = 'I:\\_Project\\DebugSrcFolder\\'
strSaveFolder = 'I:\\_Project\\DebugFolder\\'

if os.path.exists( strSaveFolder ) :
    shutil.rmtree( strSaveFolder )    #os.rmdir( strSaveFolder ) must be empty folder
    os.mkdir( strSaveFolder )  
else:
    os.mkdir( strSaveFolder )  
#######################################################################

iImageCount = 0
bPrevImageIsNotInit = True
nSkipNum = 0

while True:
    ret,img=capture.read()
    
    
    if CurrImage is None :
        print( 'Curr is None' )

        #continue
        #break
    
    break
   # CurrImage = GetImage();

    
    print( CurrImage.shape )

    ###########################################################
    if bPrevImageIsNotInit:
        PrevImage = CurrImage
        bPrevImageIsNotInit = False
        continue
    
    bImageIsEqual = ImageIsEqual( PrevImage , CurrImage )
    print( bImageIsEqual )
    PrevImage = CurrImage
    ##########################################################
    if bImageIsEqual == False :
        CurrImage = GetImage() 
        CurrImage = GetImage()
    
        PrevImage = CurrImage
        ##########################################################
        strSaveFile = strSaveFolder + "%05d.png" % (iImageCount)
        cv.imwrite( strSaveFile , CurrImage )
        iImageCount = iImageCount + 1
        print( "Save %s images" % ( strSaveFile) )


        
    
    if iImageCount > 200 :
        break

capture.release()
        
        


