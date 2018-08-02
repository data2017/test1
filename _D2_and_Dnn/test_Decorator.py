# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:09:02 2017

@author: temp
"""

def func1():
    print( 'I am function func11' )
def func2():
    print( 'I am function func22' )
    
def de( f ):
    def _call_():
        print( '-------------------------------' )
        f()
        print( '###############################' )
        return 1
        #return 
        
    return _call_



@de
def func1():
    print( 'I am function func1' )
    return 0
@de
def func2():
    print( 'I am function func2' )
    return 0
    
if __name__ == '__main__':
    a= func1()
    b = func2()