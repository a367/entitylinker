#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainList(QListWidget):
    def __init__(self, parent=None):
        QListWidget.__init__(self,parent)

        self.setMaximumWidth(170)
        self.setMinimumWidth(170)

        p = self.palette()
        p.setColor(QPalette.Text,QColor(255,255,255))
        p.setColor(QPalette.Base,QColor(39,39,39))
        self.setPalette(p)

        self.setFont(QFont(u"微软雅黑",13))

        self.setFrameShape(QListWidget.NoFrame)
        self.verticalScrollBar().setStyleSheet(open('../qss/ScrollBarStyle.qss','r').read())


