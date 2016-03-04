#coding=utf8
import sys
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from table import tableManager
from MainList import MainList
from TitlteBar import TitleBar
from MainTable import MainTable
reload(sys)
sys.setdefaultencoding('utf8')


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
    
        self.setWindowTitle(u'Entity Linker')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon("../icon/linker_01.png"))
        p = self.palette()
        p.setColor(QPalette.Background,QColor(34,34,34))
        self.setPalette(p)



        # 整体布局器
        widget = QWidget()
        self.setCentralWidget(widget)

        ## 主要布局
        mainLayout=QVBoxLayout()  
        mainLayout.setSpacing(0)

        self.titlebar = TitleBar()
        self.titlebar.setMainWindow(self)

        ### 表格的布局
        table_layout = QHBoxLayout()

        self.table = MainTable()
        self.list = MainList()
        self.list.connectTable(self.table)

        table_layout.addWidget(self.list)
        table_layout.addWidget(self.table)

        ## 主布局添加
        mainLayout.addWidget(self.titlebar)
        mainLayout.addLayout(table_layout)   

        # 整体布局器加入   
        widget.setLayout(mainLayout) 

        self.reedTables()
        #self.resize(960,640)
        self.resize(1500,1200)
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

    def reedTables(self):
        tables = tableManager().getTable()
        self.table.setTables(tables)

        for i in range(len(tables)):
            self.list.feedTitle(u'第%d个表格'%(i+1))

        self.table.displayTable(0)
        self.list.setCurrentRow(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    app.exec_()