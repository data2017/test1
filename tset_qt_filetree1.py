#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:42:33 2018

@author: nvidia
"""

    def setBrowerPath(self): 
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,  
                                    "浏览",  
                                    "E:\workspace")   
        self.lineEdit.setText(download_path)  
        
        https://blog.csdn.net/xiaoyangyang20/article/details/70268229?locationNum=3&fps=1   python3+PyQt5 树中表达表格数据