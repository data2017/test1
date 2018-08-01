#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 10:48:14 2018

@author: nvidia
"""

def xrange( start , step , end ):
    result = start
    while result < end :
        yield result
        result += step


def TestPara1( first , *args ):
    print( type( args ) )
    print( args )
    
 
def TestPara2(  first , **args ):
    print( type( args ) )
    print( args )

def TestPara3( *agrs , **kwargs ):
    print( args )
    print( kwargs )
    

temp = xrange( 0 , 2 , 10 )
print( type(temp) )

TestPara1( 1 , 2 , '2' )

TestPara2( 1 , 2 , para13='2' )
TestPara2( 1 , para2=2 , para3='2' )

TestPara2( 1 , 2 , para13='2' )
