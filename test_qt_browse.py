#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:02:21 2018

@author: nvidia
"""


#-*- coding:utf8 -*-
 


from PyQt5.QtCore import (QEvent, QObject, QFile, QFileInfo, QIODevice, QRegExp, QTextStream,Qt)

from PyQt5.QtWidgets import (QSplitter,QListView,QTreeView,QTableView,QAction, QApplication,  QFileDialog, QMainWindow, QMessageBox, QTextEdit, QFrame, QDirModel)

from PyQt5.QtGui import QFont, QIcon,QColor,QKeySequence,QSyntaxHighlighter,QTextCharFormat,QTextCursor
from PyQt5.QtGui import QPalette, QPixmap, QColor

from PyQt5 import QtCore

import math
 
#QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))
 
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    model = QDirModel()
    
    #selModel =QItemSelectionModel(model); 
    
    mylist = QListView()
    mytree = QTreeView()
    mytable = QTableView()
    
    mytree.setModel(model)
    mylist.setModel(model)
    mytable.setModel(model)
    
    #mytree.setSelectionModel(selModel)
    #mylist.setSelectionModel(mytree.selectionModel())
    #mytable.setSelectionModel(mytree.selectionModel())
    #QObject.connectNotify
    
    #QObject.connectNotify(mytree,SIGNAL("doubleClicked(QModelIndex)"),mylist.setRootIndex)
    #QObject.connectNotify(mytree,SIGNAL("doubleClicked(QModelIndex)"),mytable.setRootIndex)
    
    
    #QObject.connect(mytree,SIGNAL("doubleClicked(QModelIndex)"),mylist.setRootIndex)
    #QObject.connect(mytree,SIGNAL("doubleClicked(QModelIndex)"),mytable.setRootIndex)
    
    #######################################################
    splitter = QSplitter()
    
    splitter.addWidget(mytree )
    splitter.addWidget(mylist )
    splitter.addWidget(mytable)
    
    splitter.setWindowTitle(splitter.tr("Model/View"))
    splitter.show()
    #######################################################
    
    sys.exit(app.exec_())