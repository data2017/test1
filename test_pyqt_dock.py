# QDockWidget嵌套布局详解-实现Visual Studio布局
import sys

from PyQt5.QtWidgets import QFileDialog,QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setDockNestingEnabled(True)              

        self.items = ['呵呵', 'aa', 'bb', 'cc', 'dd', 'ee', ]
                      
        self.init()


        #QSplitter *splitterMain = new QSplitter(Qt::Horizontal, 0); //新建主分割窗口，水平分割
        self.addDock()
        self.addDock1()

    def init(self):
        self.text = QTextEdit('主窗口')
        self.text.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.text)

        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle('QDockWidget示例')
        self.show()
        pass

    def onDockListIndexChanged(self, index):
        item = self.items[index]
        self.text.setText(item)
        pass

    def onDockListDoublClick(self,ItemData):
        print( 'test' , ItemData )
        text = ItemData.text() *3 ;
        #type( ItemData )
        #item = self.items[index]
        
        FileInfo = QFileDialog()
        self.path = FileInfo.getExistingDirectory()
        #self.pathLineEdit.setText(self.path) 
        
        self.text.setText( self.path )
        pass
    
    def addDock(self):
        dock1 = QDockWidget('DockWidget *3')
        dock1.setFeatures(QDockWidget.DockWidgetFloatable)
       #dock1.setAllowedAreas(Qt.LeftDockWidgetArea)
        dock1.setAllowedAreas(Qt.AllDockWidgetAreas)

        listwidget = QListWidget()
        listwidget.addItems(self.items)
       # listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
        listwidget.itemDoubleClicked.connect(self.onDockListDoublClick  )

        dock1.setWidget(listwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

    def addDock1(self):
        dock1 = QDockWidget('DockWidget')
        dock1.setFeatures(QDockWidget.DockWidgetFloatable)
       #dock1.setAllowedAreas(Qt.LeftDockWidgetArea)
        dock1.setAllowedAreas(Qt.AllDockWidgetAreas)

        listwidget = QListWidget()
        listwidget.addItems(self.items*5)
        listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
        
        dock1.setWidget(listwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)


def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    sys.exit(app.exec_())


# 入口
if __name__ == '__main__':
    main()