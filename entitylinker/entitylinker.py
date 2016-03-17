#coding=utf8
import sys
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Function.WidgetManager import WidgetManager
from Item.ToolBar import ToolBar
from Item.TitlteBar import TitleBar

reload(sys)
sys.setdefaultencoding('utf8')


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
    
        self.setWindowTitle(u'Entity Linker')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("../icon/linker_01.png"))
        p = self.palette()
        p.setColor(QPalette.Base,QColor(34,34,34))
        p.setColor(QPalette.Background,QColor(34,34,34))
        self.setPalette(p)


        # 整体布局器
        widget = QWidget()
        self.setCentralWidget(widget)

        ## 主要布局
        mainLayout=QVBoxLayout()  
        mainLayout.setMargin(0)
        mainLayout.setSpacing(0)

        ### 标题栏，工具栏，主窗口

        self.WidgetManager = WidgetManager()


        self.titlebar = TitleBar()
        self.titlebar.setMainWindow(self)

        self.toolbar = ToolBar()
        self.toolbar.setWidgetManager(self.WidgetManager)

        ## 主布局添加
        mainLayout.addWidget(self.titlebar)
        mainLayout.addWidget(self.toolbar)
        for v in self.WidgetManager.WidgetDict.itervalues():
            mainLayout.addWidget(v)

        # 整体布局器加入   
        widget.setLayout(mainLayout) 

        self.resize(1060,840)
        
        #self.resize(1560,1340)
        self.center()

    # 居中显示
    def center(self):
        screenGeometry = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screenGeometry.width() - size.width()) / 2,
                  (screenGeometry.height() - size.height()) / 2)

    # 关闭界面
    def exit(self):
        sys.exit(0)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    app.exec_()