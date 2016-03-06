#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Item.MainList import MainList
from Item.MainTable import MainTable
from Function.table import tableManager

class ListWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        

        layout = QHBoxLayout()

        self.table = MainTable()
        self.list = MainList()
        self.list.connectTable(self.table)

        layout.addWidget(self.list)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.setMinimumWidth(840)
        
    def readTables(self):
        tables = tableManager().getTable()
        self.table.setTables(tables)

        for i in range(len(tables)):
            self.list.feedTitle(u'第%d个表格'%(i+1))

        self.table.displayTable(0)
        self.list.setCurrentRow(0)