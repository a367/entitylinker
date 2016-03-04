#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from table import tableManager

class MainTable(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
         
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setDefaultSectionSize(50)
        self.setShowGrid(False)
        self.setAutoFillBackground(True)
        self.setFont(QFont(u"微软雅黑",15))

        p = self.palette()
        p.setColor(QPalette.Text,QColor(255,255,255))
        p.setColor(QPalette.Base,QColor(34,34,34))
        p.setColor(QPalette.Background,QColor(34,34,34))
        p.setColor(QPalette.AlternateBase, QColor(39,39,39))
        self.setPalette(p)
        self.setFocusPolicy(Qt.NoFocus)
        self.setAlternatingRowColors(True);
        self.setFrameShape(QListWidget.NoFrame)
        self.setStyleSheet('QTableView {selection-background-color: #FFFFFF; selection-color: #000000;}')    
        self.verticalScrollBar().setStyleSheet(open('../qss/ScrollBarStyle.qss','r').read())
        

    # 设置table
    def displayTable(self,i):
        table = self.tables[i]
        col_count = len(table)
        row_count = len(table[0])
        self.setColumnCount(col_count)
        self.setRowCount(row_count)

        for i in range(col_count):
            for j in range(row_count):
                self.setItem(j,i,QTableWidgetItem(table[i][j]))

        self.setCurrentCell(0,0)

    def changeItem(self, index):
        item = self.item(index.column(),index.row())
        item.setBackground(Qt.white)

    # 初始化表格数据
    def setTables(self, tables):
        self.tables = tables