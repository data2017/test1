# -*- coding: utf-8 -*-
import os, sys
import numpy
import numpy as np

####################################################################################################
def ____MatInOut(): pass

def xrandint( *para ): 
    size = para[0:len(para)-1]
    low  = para[  len(para)-1][0]
    high = para[  len(para)-1][1] + 1
    #print( size )
    #print( low  )
    #print( high )
    RetValue = numpy.random.randint( low , high , size ) 
    return RetValue[0]
    
def xrandsrc( *para ):
    size = para[0:len(para)-1]
    src  = para[  len(para)-1]
    
    print( size )
    print( src  )

def xp( Mat ):
    Mat = np.mat( Mat )
    for iRow in range( Mat.shape[0] ) :
        for iCol in range( Mat.shape[1] ) :
            print( '%e, ' % Mat[iRow,iCol] , end='' )
        print( '' )

####################################################################################################
def ____MatAddSubMulDivDot(): pass

def xdot( A , B ):
    A = np.mat( A )
    B = np.mat( B )
    return np.multiply( A , B )

def xsum( A ) : 
    pass

####################################################################################################
def ____ShapeOperation(): pass

def xfliplr( In ) :
    return In[ : , ::-1 ]

def xflipud( In ) :
    return In[ ::-1 , : ]

def xrotate( In , n90Degree ):
    pass

def xcombine( ArrayList ):
    pass

def xsplit( Array ):
    pass
    
####################################################################################################
def ____BitOperation() : pass

def xdec2bit( nDec , nBitNum ) :
    assert( nBitNum <= 8 )
    arrBit = np.zeros( nBitNum , np.uint8 )
    
    for iBit in range( nBitNum ) :
        vBit = ( nDec >> (nBitNum-1-iBit) ) & (1)
        #print( nDec , end = '' )
        #print( '  ' , end ='' )
        #print( vBit , end = '' )
        #print( '' )
        arrBit[iBit] = vBit
    
    return arrBit

def xbit2dec( arrBit , nBitNum ) :
    arrBase = xfliplr( np.matlib.mat( range(nBitNum) ) )
    arrPow  = np.power( 2 , arrBase )
    
    Dot = xdot( arrBit , arrPow )
    return Dot.sum()

####################################################################################################
def xdec2bit_arr( arrIn , BitNum ):
    arrBit = np.mat( np.zeros( arrIn.size * BitNum , dtype=np.uint8 ) - 1 )
    
    iStart = 0
    #for iIter in range(List.size) :
    #    value = List[iIter]
    for value in arrIn :
        #print( value )
        SubBit = xdec2bit( value , BitNum )
        arrBit[0,iStart:iStart+BitNum] = SubBit
        iStart = iStart + BitNum
            
    return arrBit
    
def xbit2dec_arr( arrBit , BitNum ):
    nModNum = arrBit.size % BitNum
    if nModNum > 0 :
        nExtNum = BitNum - nModNum
        arrBit = np.hstack(( arrBit , np.zeros(nExtNum) ))

    arrBit = arrBit.reshape( [-1,BitNum] )
    
    List = np.zeros( arrBit.shape[0] , dtype=np.uint8 )
    for iRow in range( arrBit.shape[0] ) :
        SubBit = arrBit[iRow,:]
        Value = xbit2dec( SubBit , BitNum )
        List[iRow] = Value
        
        #print( SubBit )
        
    
    return List

####################################################################################################    

for value in range(255):
    arrBit = xdec2bit( value , 8 )
    nDec = xbit2dec( arrBit , 8 )
    diff = value - nDec
    assert( diff == 0 )
    #print( '%3d, %3d, diff=%3d' % ( value , nDec , value-nDec ) )

############################################################
for iIte in range(100) :
    RandVctOrg = xrandint( 1 , 10 , [0,255] )    
    
    arrBit     = xdec2bit_arr( RandVctOrg , 8 )
    RandVctDst = xbit2dec_arr( arrBit     , 8 )
    #print( '###################################' )
    #print( RandVctOrg )
    #print( RandVctDst )
    assert( ( RandVctOrg == RandVctDst ).all() )

############################################################
nReadCharNum = 3
strFile = '.\\test.txt'

with open( strFile , 'rb' ) as file :
    while True :
        #Block = file.read( nReadCharNum )
        Block = file.read( )  # read all
        arrDec0 = np.array( list(Block) )
        
        arrBit1 = xdec2bit_arr( arrDec0 , 8 )
        arrDec1 = xbit2dec_arr( arrBit1 , 3 )
        
        arrBit2 = xdec2bit_arr( arrDec1 , 3 )
        arrDec2 = xbit2dec_arr( arrBit2 , 8 )
        
        print( arrDec0 )
        print( arrDec1 )
        print( arrDec2 )
        break
        if len(Block) == 0 :
            break
        
        print( type( Block ) )
        print( Block )
        #print( len(Block) )
    
                


