#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Item.MainList import MainList
from Item.MainTable import MainTable
from Function.table import tableManager

class ListList(MainList):
    def __init__(self, parent = None):
        MainList.__init__(self)
        self.clicked.connect(self.changeTable)

    def connectTable(self, table):
        self.table = table
    
    def changeTable(self, item):
        self.table.displayTable(item.row())

    def feedTitle(self, title):
        item = QListWidgetItem(QIcon('../icon/list.png'),title)
        item.setSizeHint(QSize(140,40))
        self.addItem(item)

class ListWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        

        layout = QHBoxLayout()

        self.table = MainTable()
        self.list = ListList()
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