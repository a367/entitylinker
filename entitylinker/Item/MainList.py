#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainList(QListWidget):
    def __init__(self, parent=None):
        QListWidget.__init__(self,parent)

        #self.setMaximumWidth(170)
        #self.setMinimumWidth(170)

        self.setMaximumWidth(300)
        self.setMinimumWidth(300)

        p = self.palette()
        p.setColor(QPalette.Text,QColor(255,255,255))
        p.setColor(QPalette.Base,QColor(39,39,39))
        self.setPalette(p)

        self.setFont(QFont(u"微软雅黑",13))

        self.setFrameShape(QListWidget.NoFrame)
        self.verticalScrollBar().setStyleSheet(open('../qss/ScrollBarStyle.qss','r').read())
        self.clicked.connect(self.changeTable)

    def connectTable(self, table):
        self.table = table
    
    def changeTable(self, item):
        self.table.displayTable(item.row())

    def feedTitle(self, title):
        item = QListWidgetItem(QIcon('../icon/list.png'),title)
        item.setSizeHint(QSize(140,40))
        self.addItem(item)