#coding=utf8

from Widget.ListWidget import ListWidget
from Widget.CodeWidget import CodeWidget
from Widget.HtmlWidget import HtmlWidget

class WidgetManager:
    def __init__(self):
        self.WidgetDict = {}
        self.current = 'list'
        self.WidgetDict['list'] = ListWidget()
        self.WidgetDict['list'].readTables()
        self.WidgetDict['code'] = CodeWidget()
        self.WidgetDict['code'].hide()
        self.WidgetDict['html'] = HtmlWidget()
        self.WidgetDict['html'].hide()
        

    def getCurrentWidget(self):
        return self.WidgetDict[self.current]

    def changeCurrentWidget(self, name):
        self.WidgetDict[self.current].hide()
        self.WidgetDict[name].setVisible(True)
        self.current = name
