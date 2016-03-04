#coding=utf8
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class WhiteLabel(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

        self.setFont(QFont(u"微软雅黑", 12))
        self.setStyleSheet('color:#FFFFFF')


class TitleBar(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        icon = QLabel()
        icon.setPixmap(QPixmap("../icon/linker.png").scaled(1024/13,598/13))
        
        title = WhiteLabel("Entity Linker")

        btn_icon = QPushButton("XAXAXA")
        
        layout = QHBoxLayout()
        layout.addWidget(icon)
        layout.addWidget(title)
        layout.addWidget(btn_icon)
        #layout.setSpacing(0)
        layout.insertStretch(2);



        self.setLayout(layout)
        self.setMaximumHeight(70)
        self.setMinimumHeight(70)
        
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #self.resize(200,200)
    def setMainWindow(self, mainwindow):
        self.box = mainwindow

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.box.moving = True
            self.box.offset = event.pos()
    
    def mouseMoveEvent(self,event):
        self.box.move(event.globalPos()-self.box.offset)
