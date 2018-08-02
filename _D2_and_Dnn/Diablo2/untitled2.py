# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:32:13 2017

@author: temp
"""

import os
from msvcrt import getch
 
if __name__ == "__main__":
    print( "read keyboard" )
    junk = getch() # Assign to a variable just to suppress output. Blocks until key press.
    print( junk )