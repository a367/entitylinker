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
        self.verticalHeader().setDefaultSectionSize(80)
        self.setShowGrid(False)
        self.setAutoFillBackground(True)
        self.setFont(QFont("song",15))

        p = self.palette()
        p.setColor(QPalette.Text,QColor(255,255,255))
        p.setColor(QPalette.Base,QColor(0,0,0))
        p.setColor(QPalette.AlternateBase, QColor(34,34,34))
        self.setPalette(p)
        self.setAlternatingRowColors(True);

        t = tableManager()
        tables = t.getTable()
        self.feedTable(tables[0])



    # 设置table
    def feedTable(self,table):
        col_count = len(table)
        row_count = len(table[0])
        self.setColumnCount(col_count)
        self.setRowCount(row_count)

        for i in range(col_count):
            for j in range(row_count):
                self.setItem(j,i,QTableWidgetItem(table[i][j]))