import sys
from PyQt4 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Teww(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("TEww")
        self.tree=QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["key","value"])
        root=QTreeWidgetItem(self.tree)
        root.setText(0,"root")
        child1=QTreeWidgetItem(root)
        child1.setText(0,"child1")
        child1.setText(1,"name")
        child2=QTreeWidgetItem(root)
        child2.setText(0,"child2")
        child2.setText(1,"name")
        child3=QTreeWidgetItem(child2)
        child3.setText(0,"child3")
        child3.setText(1,"name")
        child4=QTreeWidgetItem(child3)
        child4.setText(0,"child4")
        child4.setText(1,"name")
        self.tree.addTopLevelItem(root)
        self.setCentralWidget(self.tree)
        self.root_2()
        self.root_3()

    def root_2(self):
        root2=QTreeWidgetItem(self.tree)
        root2.setText(0,"root2")
        child5=QTreeWidgetItem(root2)
        child5.setText(0,"child5")
        child5.setText(1,"ddd")
        self.tree.addTopLevelItem(root2)
        self.setCentralWidget(self.tree)
    def root_3(self):
        root3=QTreeWidgetItem(self.tree)
        root3.setText(0,"root3")
        child6=QTreeWidgetItem(root3)
        child6.setText(0,"child6")
        child6.setText(1,"child6")
        self.tree.addTopLevelItem(root3)
        self.setCentralWidget(self.tree)
if __name__=="__main__":
    app = QApplication(sys.argv)
    tp = Teww()
    tp.show()
    app.exec_()