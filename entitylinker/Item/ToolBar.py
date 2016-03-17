#coding=utf8
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolBtn(QToolButton):
    def __init__(self, icon, name):
        QPushButton.__init__(self)
        self.setIcon(icon)
        self.setText(name)
        self.setFont(QFont(u"微软雅黑",10))
        self.setIconSize(QSize(40,50))
        self.setCheckable(True)
        self.setAutoExclusive(True)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        p = self.palette()
        p.setColor(QPalette.ButtonText,QColor(255,255,255))
        self.setPalette(p)




class ToolBar(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.setStyleSheet(open("../qss/ToolBarStyle.qss",'r').read())
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(QPalette.Background,QColor(49,49,49))
        self.setPalette(p)


        btn_list = ToolBtn(QIcon("../icon/tool_list.png"), "list")
        btn_list.setChecked(True)
        btn_list.clicked.connect(lambda: self.changeFrame('list'))

        btn_html = ToolBtn(QIcon("../icon/html.png"), "html")
        btn_html.clicked.connect(lambda: self.changeFrame('html'))

        btn_text = ToolBtn(QIcon("../icon/text.png"), "text")
        btn_import = ToolBtn(QIcon("../icon/import.png"), "import")

        btn_code = ToolBtn(QIcon("../icon/code.png"), "code")
        btn_code.clicked.connect(lambda: self.changeFrame('code'))

        btn_work = ToolBtn(QIcon("../icon/work3.png"), "run")


        layout = QHBoxLayout()

        layout.addWidget(btn_list)
        layout.addWidget(btn_html)
        layout.addWidget(btn_text)
        layout.addWidget(btn_import)
        layout.addWidget(btn_code)
        layout.addWidget(btn_work)
        layout.setMargin(0)
        layout.setSpacing(0)

        self.setLayout(layout)       
        self.setMaximumHeight(65)
        self.setMinimumHeight(65)
       
    def changeFrame(self, name):
        self.widgetMgr.changeCurrentWidget(name)

    def setWidgetManager(self, widgetManager):
        self.widgetMgr = widgetManager