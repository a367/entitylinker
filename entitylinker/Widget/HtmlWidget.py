#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from Item.MainList import MainList
from Function.LexerManager import LexerManager

class HtmlList(MainList):
    def __init__(self, parent = None):
        MainList.__init__(self)
        self.clicked.connect(self.changeViewer)
        #QModelIndex().data().toString()


    def connectViewer(self, viewer):
        self.viewer = viewer

    def changeViewer(self, item):
        filename = str(item.data().toString())
        self.viewer.setCode(filename)

    def feedTitle(self, title):
        item = QListWidgetItem(QIcon('../icon/list.png'),title)
        item.setSizeHint(QSize(140,40))
        self.addItem(item)

class HtmlViewer(QWebView):
    def __init__(self, *args):
        QWebView.__init__(self)
        self.HtmlLex = LexerManager('html')

    def setCode(self, filename):
        self.setHtml(self.HtmlLex.getCode(filename))

    def getCodelist(self):
        return self.HtmlLex.codeDict.keys()


class HtmlWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.list = HtmlList()
        self.htmlView = HtmlViewer()
        self.list.connectViewer(self.htmlView)

        for filename in self.htmlView.getCodelist():
            self.list.feedTitle(filename)

        layout.addWidget(self.list)
        layout.addWidget(self.htmlView)

        self.setLayout(layout)
        self.setMinimumWidth(840)



