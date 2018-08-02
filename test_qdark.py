#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:36:00 2018

@author: nvidia
"""

import sys
import qdarkstyle
from PyQt5 import QtWidgets

def main() :
    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QMainWindow()
    
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    # run
    window.show()
    
    app.exec_()
    
    
main()    