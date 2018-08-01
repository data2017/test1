# -*- coding: utf-8 -*-


download_path = QtWidgets.QFileDialog.getExistingDirectory(self,  
                                    "浏览",  
                                    "E:\workspace")   
self.lineEdit.setText(download_path)  
self.edit = QtGui.QLineEdit(self)#创建 QLineEdit 。
 
self.edit.move(60, 100)#文本框的位置
 
self.connect(self.edit, QtCore.SIGNAL('textChanged(QString)'),self.onChanged)
#如果单行编辑器中的文本发生变化，调用 onChanged() 方法。
 
self.setWindowTitle('QLineEdit')
self.setGeometry(250, 200, 350, 250)


