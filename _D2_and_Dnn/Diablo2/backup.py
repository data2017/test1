# -*- coding: utf-8 -*-

for i in np.arange( 1 , 2 , 1 ):
    i = 1
    print( i )
 
    #continue;
    StartGame( 'rr'+ str(i) ); 
    time.sleep( 0.5 )
    
    
    #CreateAcc( AccName , Pass )
    LoginAcc( AccName , Pass )
    time.sleep( 0.5 )
    
    CreateChar( 'bar' , 'bdrrbar_b' , 1 , 1  )
    
    
    
def TestMove():
    ## get win rect and move to top-left position
    hWnd =win32gui.FindWindow(0, 'D2Loader v1.11b - Build On Nov 11 2005' )
    rect = win32gui.GetWindowRect( hWnd )
    sim.moveTo( rect[0] , rect[1] , duration=0.25 )
    
    sim.moveRel( 200 , 200 , duration=0.25 )
    sim.click(button='left')
#StartGame( 'rr2' ); time.sleep( 0.1 )
#StartGame( 'rr3' ); time.sleep( 0.1 )

#######################################
#LoginAcc( 'bdbdsor'  , 'imustsucceed' , 'rb00' , '' )
#time.sleep( 2.0 )

#######################################
#SelectChar( 'testname'  )

#######################################
#CreateGame( 'rb01' , 'normal' , 'password' )


#######################################
#TestMove()


#######################################
        #pyautogui.click(button='left') # 点击鼠标左键  
        #pyautogui.doubleClick() #双击  
#pyautogui.moveTo(100,100,duration=0.25)
#         pyautogui.moveRel(100,0,duration=0.25)
#pyautogui.position()




#print( rect )