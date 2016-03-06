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

        self.setStyleSheet(open("../qss/TitleBarStyle.qss",'r').read())

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(QPalette.Background,QColor(39,39,39))
        self.setPalette(p)

        # 控件设置
        icon = QLabel()
        icon.setPixmap(QPixmap("../icon/linker.png").scaled(1024/20,598/20))
        
        title = WhiteLabel("Entity Linker 1.0 Ultimate")

        btn_close = QToolButton(self)
        btn_close.setIcon(QIcon("../icon/close.png"))
        btn_close.setIconSize(QSize(20,30))
        btn_close.clicked.connect(self.close)
        
        btn_min = QToolButton(self)
        btn_min.setIcon(QIcon("../icon/min.png"))
        btn_min.setIconSize(QSize(20,30))
        btn_min.clicked.connect(self.min)

        btn_max = QToolButton(self)
        btn_max.setIcon(QIcon("../icon/max.png"))
        btn_max.setIconSize(QSize(20,30))
        btn_max.clicked.connect(self.max)
        self.max_flag = False

        btn_menu = QToolButton(self)
        btn_menu.setIcon(QIcon("../icon/menu.png"))
        btn_menu.setIconSize(QSize(20,30))
        
        # 布局设置
        layout = QHBoxLayout()
        layout.addWidget(icon)
        layout.addWidget(title)
        layout.addWidget(btn_menu)
        layout.addWidget(btn_min)
        layout.addWidget(btn_max)
        layout.addWidget(btn_close)
        layout.insertStretch(2);
        self.setLayout(layout)
        self.setMaximumHeight(40)
        self.setMinimumHeight(40)
        
    def min(self):
        self.box.showMinimized()

    def max(self):
        if self.max_flag:
            self.box.showNormal()
        else:
            self.box.showMaximized()
        self.max_flag = not self.max_flag

    def close(self):
        self.box.exit()

    def setMainWindow(self, mainwindow):
        self.box = mainwindow

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.box.moving = True
            self.box.offset = event.pos()
    
    def mouseMoveEvent(self,event):
        self.box.move(event.globalPos()-self.box.offset)
