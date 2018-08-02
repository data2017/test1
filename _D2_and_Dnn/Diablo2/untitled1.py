# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:12:00 2017

@author: temp
"""

import win32gui

def callback(hwnd, extra):
    print( hwnd )
    
    return
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print( "Window %s:" %win32gui.GetWindowText(hwnd) )
    print( "\tLocation: (%d, %d)" % (x, y) )
    print( "\t    Size: (%d, %d)" % (w, h) )

def main():
    win32gui.EnumWindows(callback, None)

if __name__ == '__main__':
    main()
    
hWnd =win32gui.FindWindow(0, 'Spyder (Python 3.6)' )
rect = win32gui.GetWindowRect( hWnd )
print( rect )
