# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:18:52 2017

@author: temp
"""



# LoadGame( acc,pw,char, 'create' , name, , title , strMode )
# LoadGame( acc,pw,char, 'join'   , gamename , title , strMode )
def LoadGame( Acc,Pass,Char, Action,Game,Difficulty, Title,Mode )
    
    
    
    Login( Acc , Pass , Title , Mode )
    Act( Char , Action , Game , Difficulty)
    
    SendKey( 'Tab',Acc , 'Tab',Pass , 'Enter' )
    
    GotoChar( 'name' to idx ); //-->Sendkey( 'Left' or 'Right' )
    
    SendKey( 'Tab' , Pass )
    
    if( 0 ):
        strAcc = '' #' -bnacct bdbdsorqh -bnpass imustsucceed '
        if 1 :#strMode=='Normal':
            print( strNormal  +strAcc )
            win32api.ShellExecute(0, 'open', strD2 , strNormal  +strAcc ,'',1); 
        else:
            time.sleep(0.5)
        
#******************************************************************************
    
LoadGame( 'bdbdbo','imustsucceed','', 'create','uupp1','normal', '','' )


aaa
LoadGame( 'bdbdbo','imustsucceed','', 'create','uupp1','normal', '','' )

df = DataFrame(columns=('lib', 'qty1', 'qty2'))#生成空的pandas表  
for i in range(5):#插入一行<span id="transmark" style="display: none; width: 0px; height: 0px;"></span>  
    df.loc[i] = [ 0+i*10, 1+i*10, 2+i*10 ]  
print( df  )

