#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:41:51 2018

@author: nvidia
"""
 

for bitnum in [8,16,32,64] :
    print( 'typedef int%d_t  int%d ;' % ( bitnum , bitnum) )
    print( 'typedef uint%d_t uint%d;' % ( bitnum , bitnum) )
    
print( '' );
    
print( 'typedef float  flt32;' );
print( 'typedef double flt64;' );


arrList = ['int8' 'int16' 'int32' 'int64' ]
for strType in arrList :
    print( 'mxArray* mxx%s( const std::vector<%s>& vct)' %( strType , strType) )
    strType.capitalize()