#friend: Drop_jj

import os, sys
import AccCharOperation

class CAccInfo:
    def __init__(self):
        self.AccInfo  = ''
        self.Acc      = ''
        self.Pass     = '' 
        self.CharList = []  
        
AccInfo = []
strAccList = []
         #acc         pass             char1 char2 char3 char4 char5 char6 char7 char8
Info=[ 'bdbdmain'  , 'imustsucceed' , 'bdnec'   , '' , '', '', '', '', '', '']; AccInfo.append( Info )
Info=[ 'bdbdmain1' , 'imustsucceed' , 'bdneca'  , '' , '', '', '', '', '', '']; AccInfo.append( Info )
Info=[ 'bdbdmain2' , 'imustsucceed' , 'bdneca'  , '' , '', '', '', '', '', '']; AccInfo.append( Info )
Info=[ 'bdbdsor'   , 'imustsucceed' , 'bdsor'   , '' , '', '', '', '', '', '']; AccInfo.append( Info )

Info=[ 'bdbdbo'    , 'imustsucceed' , 'bdbo'    , '' , '', '', '', '', '', '']; AccInfo.append( Info )
Info=[ 'bdbdqh'    , 'imustsucceed' , 'bdbdnec' , '' , '', '', '', '', '', '']; AccInfo.append( Info )
Info=[ 'bdbdpal1'  , 'imustsucceed' , 'bdbdnec' , '' , '', '', '', '', '', '']; AccInfo.append( Info )
    

def ConstructAccInfo():
    AccList = []
    for Info in AccInfo:
        iCharOffset = 2;
        Temp = CAccInfo()
        
        Temp.Acc  = Info[0]
        Temp.Pass = Info[1]
        for iChar in range(8) :
            Temp.CharList.append( Info[iCharOffset+iChar] )
            
        #print( Temp )
        AccList.append( Temp )
    return AccList

def GenerateKeyAcc():
    NamePrefix = 'bdkey'
    NameSuffix = 'bd'
    Pass = 'uxthb1766'


    #print( D2Game.hWnd )
    
    #for iChar in range(4):
    for iChar in range(2,4):
        D2Game = AccCharOperation.CD2Game()
        D2Game.StartProgram( 'Normal' )
        
        iCharIdx = iChar + 1
        AccName = NamePrefix + "%d"%iCharIdx + NameSuffix
        CharName1 = NamePrefix + NameSuffix + 'zlp' + chr(ord('a')+iChar)
        CharName2 = NamePrefix + NameSuffix + 'fzl' + chr(ord('a')+iChar)
        
        print( 'loc3984' , AccName , CharName1 , CharName2 )
        
        D2Game.CreateAcc( AccName , bdkeybdzlpcPass )
        #D2Game.LoginAcc( AccName , Pass )
        D2Game.CreateChar( 'bar' , CharName1 , IsFz=0 , IsHardCore=1 )
        D2Game.CreateChar( 'bar' , CharName2 , IsFz=1 , IsHardCore=1 )
        
        D2Game.ExitProgram()

        
################################
AccList = ConstructAccInfo()

GenerateKeyAcc()
#Prefix = ''
#strKeyAccList = []

sys.exit()

iAcc = 0
print( AccList[iAcc].Acc , '---' ,  AccList[iAcc].Pass  )

D2Game = AccCharOperation.CD2Game(  )
D2Game.StartProgram( 'nouse' )
D2Game.LoginAcc( AccList[iAcc].Acc , AccList[iAcc].Pass )


