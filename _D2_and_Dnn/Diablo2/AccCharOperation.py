# -*- coding: utf-8 -*-

from pandas import *
from random import *

import numpy as np
import pyautogui as sim
import win32gui

import time
import win32api
import os, sys
import subprocess

#strD2 = 'D:\\Games\\D2\\D2Loader.exe'
#strNormal  = ' -w -nohide -direct -pdir  map  -skiptobnet -locale chi -ns'
#strNoSound = ' -w -nohide -direct -pdir  map  -skiptobnet -locale chi -ns '

#'bdbdbo'   , 'imustsucceed' , 'bdbo'    , '' \
#bdbdsorqh
#bdbdsor
#bdbdsora


def SendKey( Key ):
    if   Key=='tab'   : sim.press( 'tab'   )
    elif Key=='enter' : sim.press( 'enter' )
    elif Key=='up'    : sim.press( 'up'    )
    elif Key=='down'  : sim.press( 'down'  )
    elif Key=='right' : sim.press( 'right' )
    elif Key=='left'  : sim.press( 'left'  )
    elif Key=='esc'   : sim.press( 'esc'   )
    elif Key=='AltF4' : sim.hotkey('altleft', 'f4')

    else              : sim.typewrite( Key )  #interval=0.25)
    
    time.sleep( 0.2 )
#end def##################################################################

def MoveClick( Point , dDuration ):
    
    dDuration = dDuration + 2;
    
    sim.moveTo( Point[0] , Point[1] , duration=dDuration )
    sim.click( button='left' )


def GenerateRandEmail():
     #email_suffix = "@gmail.com,@yahoo.com,@msn.com,@hotmail.com,@aol.com,@ask.com,@live.com,@qq.com,@0355.net,@163.com,@163.net,@263.net,@yeah.net,@googlemail.com,@126.com,@sina.com,@sohu.com,@yahoo.com.cn"
     Email = 'sss@qq.com'
     return Email
 
def xRandPoint( x , y , w , h ):
    Point = np.array( [x , y] )
    return Point
    

def ________(): pass

#end def#################################################################
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class CD2Game( object ):
    def __init__( self ):
        self.strTitle    = 'nan'
        self.strAccName  = 'nan'
        self.strAccPass  = 'nan'
        
        self.iCharIdx    = 'nan'
        self.strCharName = 'nan'
        self.strGameLvl  = 'nan'
        
        self.hWnd        = 'nan'
        

    def GetLeftTop( self ):
        hWnd = self.hWnd
        rect = win32gui.GetWindowRect( hWnd ) #self.hWnd )
        LeftTop = np.array( [ rect[0] , rect[1]+25 ] )
        #print( self.hWnd )
        return LeftTop
        
    def StartProgram( self, strTitle ):
        # -lq -ns -pdir plugina
        # -lq -ns -pdir plugina 
        # -title  -title
        # -skiptobnet: enter bn directly
        # D:\Games\D2\D2Loader.exe -w -nohide -direct -pdir plugina  -skiptobnet  -locale chi
        #WinTitle , GameMode ):
        #strLast = strNoSound + ' -title ' + WinTitle;
        ##print( strLast ); return;
        strD2Loader = 'D:\Games\D2\D2Loader.exe';
        
        strOption = ''
        strOption = strOption + ' -w -nohide -direct -pdir plugina  -skiptobnet -locale chi '
        strOption = strOption + ' -ns'
        #strOption = strOption + ' -lq'
       
        if strTitle != '':
            strOption = strOption + ' -title ' + strTitle
       
        #strD2Loader = strD2Loader + ' ' + strOption
        #print( strD2Loader )
        #strD2Loader = 'D:\Games\BaiYi';
        #strOption   = ''
        win32api.ShellExecute(0, 'open', strD2Loader , strOption ,'',1)
        
        #self.StartGame( self.strTitle )
        time.sleep( 2.0 ) #wait windows construct finished
        self.strTitle = strTitle;
        self.hWnd     = win32gui.FindWindow(0, strTitle )
        print( self.hWnd )
    
    def ExitProgram( self ):
        SendKey( 'AltF4' )

    def CreateAcc( self, AccName , Pass ):
        ## get win rect and move to top-left position
        LeftTop = self.GetLeftTop()
        
        #sim.moveTo( rect[0] , rect[1] , duration=0.25 )
        
        ##################################################
        RectLogin    = xRandPoint( 390, 469, 80, 8 ) +LeftTop
        RectConfig   = xRandPoint( 390, 515, 80, 8 ) +LeftTop 
        RectCreate   = xRandPoint( 390, 555, 80, 8 ) +LeftTop 
        
        RectAgree    = xRandPoint( 586, 497, 30, 9 ) +LeftTop 
        RectNamePsOk = xRandPoint( 684, 556, 30, 9 ) +LeftTop 
        
        RectTimeOk   = xRandPoint( 558, 497, 30, 9 ) +LeftTop   
        
        RectEmailOk     = xRandPoint( 390, 510, 30, 9 ) +LeftTop 
        RectEmailCancel = xRandPoint(  82, 555, 30, 9 ) +LeftTop 
        
        RectEmailNoNeed         = xRandPoint( 390, 557, 30, 9 ) +LeftTop 
        RectEmailNoNeedCancel   = xRandPoint( 315, 397, 30, 9 ) +LeftTop 
        RectEmailNoNeedContinue = xRandPoint( 475, 397, 30, 9 ) +LeftTop 
        #########################################
        
        #time.sleep( 10 )
        ## move to "create" and "click"
        #sim.moveRel(600,490,duration=0.25)
        #sim.click(button='left')
        #time.sleep( 0.25 )        
        
        MoveClick( RectCreate  , 0.25 ) 
        MoveClick( RectAgree   , 0.25 )
        
    
        SendKey( 'tab' )
        SendKey( 'tab' )
        
        #input name
        SendKey( AccName )
        #input pass
        SendKey( 'tab' )
        SendKey( Pass )
        SendKey( 'tab' )
        SendKey( Pass )
        #click OK button
        MoveClick( RectNamePsOk  , 0.25 )
    
        #click time-duration button
        MoveClick( RectTimeOk , 0.25  )
    
        #input email twice
        Email = GenerateRandEmail()
        SendKey( 'tab' )    
        SendKey( Email )
        SendKey( 'tab' )    
        SendKey( Email )
        
        MoveClick( RectEmailOk , 0.25 )
    
    #GameMode = no soundqh or low quality and so on
    def LoginAcc( self, Acc , Pass ):
        
        time.sleep( 1.5 )    
        SendKey( 'tab'   );  SendKey( Acc  );
        SendKey( 'tab'   );  SendKey( Pass );
        SendKey( 'enter' );
        time.sleep( 1.5 )

        
    #end def##################################################################
    
    def ________(): pass
    
    def CreateChar( self, CharType , CharName ,  IsFz , IsHardCore ):
        #select char type
        rect = win32gui.GetWindowRect( self.hWnd )
        LeftTop = np.array( [ rect[0] , rect[1]+25 ] )
        
        CreateCharPoint = xRandPoint( 120, 500, 40, 15 ) +LeftTop
        
        amaPoint = xRandPoint( 100,300, 10, 30 ) +LeftTop
        asnPoint = xRandPoint( 200,300, 10, 30 ) +LeftTop
        necPoint = xRandPoint( 300,300, 10, 30 ) +LeftTop
        barPoint = xRandPoint( 400,270, 10, 30 ) +LeftTop
        palPoint = xRandPoint( 525,270, 10, 30 ) +LeftTop
        sorPoint = xRandPoint( 620,300, 10, 30 ) +LeftTop
        druPoint = xRandPoint( 710,300, 10, 30 ) +LeftTop
        
        PointList = [ amaPoint, asnPoint, necPoint, barPoint, palPoint, sorPoint, druPoint ]
        NameList  = [ 'ama'   , 'asn'   , 'nec'   , 'bar'   , 'pal'   , 'sor'   , 'dru'    ]
        
        zlpPoint = xRandPoint( 325,534,  5,  5 ) +LeftTop
        hcPoint  = xRandPoint( 325,552,  5,  5 ) +LeftTop
        
        okPoint       = xRandPoint( 685,557, 30,  8 ) +LeftTop
        DeadWarnPoint = xRandPoint( 465,321, 30, 8 ) +LeftTop
        ###################################################################s
        
        # click create button
        MoveClick( CreateCharPoint , 0.25 )
        
        # select char type
        for iChar in range(len(NameList)):
            if NameList[iChar]==CharType:
                MoveClick( PointList[iChar] , 0.25 )
                break
        
        # enter char-name
        SendKey( CharName )
        
        #
        if IsFz:
            MoveClick( zlpPoint , 0.25 )
     
        #
        if IsHardCore:
            MoveClick( hcPoint , 0.25  )
                      
        # move to "ok" button and click
        MoveClick( okPoint , 0.25 )
        # click hc death warning button
        MoveClick( DeadWarnPoint , 0.25 )
    
        SendKey( 'esc' )
        time.sleep( 2.0 ) #wait to exit from game-interface to char-interface
        
    def ConvertChar( self, CharName ):
        pass
    
    def DelChar( self, CharName ):
        pass
    
    def SelectChar( self, Char ):
        #relocation at left-top
        #SendKey( 'right' ); SendKey( 'up' ); SendKey( 'up' ); SendKey( 'up' );
        
        #nRow,nCol = GetCharPos( Char )
        #nRow = 2; nCol = 2;
     
        #move select box to specific char
        #if nCol == 2 : 
        #    SendKey( 'right' )
        
        #for iRow in range(nRow):
        #    SendKey( 'down' )
        
        #select and enter "create" or "join" interface
        SendKey( 'enter' ); 
        time.sleep( 1.0 )
        ###########################################
    #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def ________():
        pass
        
    #, Action , Game , Difficult
    def CreateGame( self, GameName , GameLvl , GamePass ):
        ## get win rect and move to top-left position
        LeftTop = self.GetLeftTop()

        CreatePoint = xRandPoint( 560,460 , 35,5 ) +LeftTop
        
        PtPoint = xRandPoint( 437,373 , 35,5 ) +LeftTop
        EmPoint = xRandPoint( 563,373 , 35,5 ) +LeftTop
        DyPoint = xRandPoint( 560,460 , 35,5 ) +LeftTop
        
        OkPoint = xRandPoint( 706,373 , 35,5 ) +LeftTop
        
        dDuration = 0.20
        ## move to "create" and "click"
        MoveClick( CreatePoint , dDuration )
    
        ## input game-name 
        time.sleep( 0.1 )
        SendKey( GameName )
        SendKey( 'tab' ) # note it is need to make GameName box accepting input
        
        ## move to "normal-nightmare-hell" button and "click"
        if  GameLvl=='pt': 
            MoveClick( PtPoint , dDuration )
        elif GameLvl=='em':
            MoveClick( EmPoint , dDuration )
        elif GameLvl=='dy':
            MoveClick( DyPoint , dDuration )
        else:
            print( 'GameLvel should be pt or em or dy' )
            return;
        ## move to "create game" button and "click"
        SendKey( 'enter' )
        #MoveClick( OkPoint , dDuration )

    
    #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def JoinGame( self, GameName, GamePass ):
        LeftTop = self.GetLeftTop()
        JointPoint = xRandPoint( 660,460 , 35,5 ) +LeftTop;
        
        MoveClick( JointPoint , 0.25 )
        
        time.sleep( 0.1 )
        SendKey( GameName )
        SendKey( 'tab' ) # note it is need to make GameName box accepting input
        SendKey( GamePass )
        SendKey( 'tab' ) 

        SendKey( 'enter' )
    
def ________(): pass


#end def##################################################################

if 0: #__name__ == "__main__":
    #print( 'exit' ); sys.exit( 0 )
    
    #for i in np.arange( 1 , 8 , 1 ):
    
    D2Game = CD2Game( 'rr1' )
    
    i = 1;
    AccName = 'bdbdxtrr' + str(i)
    AccPass = 'psrr1' 
    
    CharName = ''
    
    GameName = 'su121'
    GameLvl  = 'pt'
    GamePass = ''
    
    D2Game.LoginAcc( AccName , AccPass )
    D2Game.SelectChar( CharName )
    D2Game.JoinGame( GameName , GamePass )
    #D2Game.CreateGame( GameName , GameLvl , GamePass )
else:
    print( __name__ , 'is import, not as main' )
