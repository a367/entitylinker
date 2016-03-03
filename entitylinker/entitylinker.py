#coding=utf8
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from table import tableManager
reload(sys)
sys.setdefaultencoding('utf8')


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
    
        self.setWindowTitle(u'Entity Linker')



        # MenuBar
        menubar = self.menuBar()
        file = menubar.addMenu(u'文件')
        fileopen = file.addAction(u'打开')
        filexit = file.addAction(u'退出')
        filexit.setShortcut('Ctrl+Q')
        self.connect(filexit, SIGNAL('triggered()'), self.exit)

        #p = menubar.palette()
        #p.setColor(QPalette.Text,QColor(255,255,255))
        #p.setColor(QPalette.Base,QColor(34,34,34))
        #menubar.setPalette(p)


        self.setMenuBar(menubar)


        # 整体布局器
        widget = QWidget()
        self.setCentralWidget(widget)

        ## 主要布局
        mainLayout=QVBoxLayout()  

        ### 表格
        self.table = QTableWidget()   
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.table.resizeRowsToContents()
        self.table.setShowGrid(False)
        self.table.setAutoFillBackground(True)
        self.table.setFont(QFont("song",15))
        self.table.setStyleSheet("QTableWidget::item:selected { background-color: rgb(255, 255, 255) }");

        p = self.table.palette()
        p.setColor(QPalette.Text,QColor(255,255,255))
        p.setColor(QPalette.Base,QColor(34,34,34))
        self.table.setPalette(p)


        t = tableManager()
        tables = t.getTable()
        self.setTable(tables[0])


        ## 主布局添加
        mainLayout.addWidget(self.table) 

        # 整体布局器加入   
        widget.setLayout(mainLayout) 


        self.resize(960,640)
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

    # 放置表格
    def setTable(self,table):
        col_count = len(table)
        row_count = len(table[0])
        self.table.setColumnCount(col_count)
        self.table.setRowCount(row_count)

        for i in range(col_count):
            for j in range(row_count):
                self.table.setItem(j,i,QTableWidgetItem(table[i][j]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()

    app.exec_()