#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:06:52 2018

@author: nvidia
"""

class Person() : 
    count = 0;
    def __init__(self,name):
        self.name = name
        
    def get_myname(self):
        return self.name
    
class SuperMan( Person ):
    def __init__(self,name):
        #self.name   = name + 'super'
        super().__init__( name )
        self.weapon = 'super weaapon'
        

   
    def get_name(self):
        return self.name
    
hunter = Person( 'sqwu' )        
print( '####' , hunter.name )
#print( '####' , hunter.myname )

superman = SuperMan( 'sqwu1' )

print( '####' , superman.name , ';' , superman.weapon )



print( '####' , superman.get_name() )
print( '####' , superman.get_myname() )
#print( '####' , superman.myname )
