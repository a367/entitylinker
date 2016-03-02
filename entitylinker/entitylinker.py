#coding=utf8
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
reload(sys)
sys.setdefaultencoding('utf8')

#class MyDialog(QDialog):

#    def __init__(self, parent=None):
#        QDialog.__init__(self,parent)

#        self.quit = QPushButton("Quit")
#        self.change = QPushButton("Change")
#        self.change.setEnabled(False)

#        # funny widget
#        self.lcd = QLCDNumber(2)
 
#        self.slider = QSlider(Qt.Horizontal)
#        self.slider.setRange(0, 99)
#        self.slider.setValue(0)
         
#        self.lineEdit = QLineEdit()
#        intValidator = QIntValidator(0,99,self)
#        self.lineEdit.setValidator(intValidator) 



#        self.connect(self.quit, SIGNAL("clicked()"),
#                    qApp, SLOT("quit()"))
#        self.connect(self.lineEdit, SIGNAL("textChanged(const QString&)"),
#                    self.enableChangeButton)
#        self.connect(self.slider, SIGNAL("valueChanged(int)"),
#                    self.SliderChange)
#        self.connect(self.change, SIGNAL("clicked()"),
#                    self.Change)
         
#        self.rightLayout = QVBoxLayout()
#        self.rightLayout.addWidget(self.lineEdit)
#        self.rightLayout.addWidget(self.change)
         
#        self.leftLayout = QVBoxLayout()
#        self.leftLayout.addWidget(self.lcd)
#        self.leftLayout.addWidget(self.slider)
         
#        self.layout = QHBoxLayout()
#        self.layout.addWidget(self.quit)
#        self.layout.addLayout(self.leftLayout)
#        self.layout.addLayout(self.rightLayout)
         
#        self.setLayout(self.layout);

#    def enableChangeButton(self, text):
#        self.change.setEnabled(text.isEmpty() == False)
 
#    def Change(self):
#        value = int(self.lineEdit.text())
#        self.lcd.display(value)
#        self.slider.setValue(value)
 
#    def SliderChange(self):
#        value = self.slider.value()
#        self.lcd.display(value)
#        self.lineEdit.setText(str(value))


#class Icon(QMainWindow):
#    def __init__(self, parent=None):
#        super(Icon, self).__init__(parent)
 
#        # MenuBar
#        menubar = self.menuBar()
#        file = menubar.addMenu(u'文件')
#        fileopen = file.addAction(u'打开')
#        fileopen.setStatusTip(u'打开文件')
#        filexit = file.addAction(u'退出')
#        filexit.setShortcut('Ctrl+Q')
#        self.connect(filexit, SIGNAL('triggered()'), self.exit)
#        self.setMenuBar(menubar)
 
#        # ToolBar
#        editToolbar = self.addToolBar(u'设置')
#        newTool = editToolbar.addAction( u'新建')
#        saveTool = editToolbar.addAction( u'保存')
#        self.connect(saveTool, SIGNAL('triggered()'), self.save)
 
#        exit = QPushButton('Exit', self)
#        exit.setGeometry(30, 100, 50, 30)
#        exit.setToolTip(u'点击按钮关闭窗口')
#        self.connect(exit, SIGNAL('clicked()'), self.exit)
 
#        # 设置窗口大小已经位置
#        self.resize(350, 250)
#        self.center()
 
#        self.statusBar().showMessage(u'准备就绪')
#        self.setWindowIcon(QIcon('logo.png'))
#        self.setWindowTitle('PyQt4 Demo')
 
#    def closeEvent(self, event):
#        replay = QMessageBox.question(
#            self, u'温馨提示', u'是否确定关闭窗口', QMessageBox.Yes, QMessageBox.No)
#        if replay == QMessageBox.Yes:
#            event.accept()
#        else:
#            event.ignore()
 
#    def save(self):
#        replay = QMessageBox.question(
#            self, u'温馨提示', u'是否进行保存', QMessageBox.Yes, QMessageBox.No)
 
#    def exit(self):
#        sys.exit(0)
 
#    def center(self):
#        screenGeometry = QDesktopWidget().screenGeometry()
#        size = self.geometry()
#        self.move((screenGeometry.width() - size.width()) / 2,
#                  (screenGeometry.height() - size.height()) / 2)
 

#class Palette(QDialog):  

#    def __init__(self,parent=None):  
#        QDialog.__init__(self,parent)  
#        self.setWindowTitle(self.tr("QPalette对话框"))  
  
#        mainLayout=QHBoxLayout(self)  
#        self.ctrlFrame=QFrame()  
#        self.contentFrame=QFrame()  
#        self.contentFrame.setAutoFillBackground(True)  
#        self.createCtrlFrame()  
#        self.createContentFrame()  
#        mainLayout.addWidget(self.ctrlFrame)  
#        mainLayout.addWidget(self.contentFrame)          
  
#    def createCtrlFrame(self):  
#        label1=QLabel("QPalette.Window")  
#        self.windowComboBox=QComboBox()  
#        label2=QLabel("QPalette.WindowText")  
#        self.windowTextComboBox=QComboBox()  
#        label3=QLabel("QPalette.Button")  
#        self.buttonComboBox=QComboBox()  
#        label4=QLabel("QPalette.ButtonText")  
#        self.buttonTextComboBox=QComboBox()  
#        label5=QLabel("QPalette.Base")  
#        self.baseComboBox=QComboBox()  
  
#        self.fillColorList(self.windowComboBox)  
#        self.fillColorList(self.windowTextComboBox)  
#        self.fillColorList(self.buttonComboBox)  
#        self.fillColorList(self.buttonTextComboBox)  
#        self.fillColorList(self.baseComboBox)  
#        self.connect(self.windowComboBox,SIGNAL("currentIndexChanged(int)"),self.slotWindow)  
#        self.connect(self.windowTextComboBox,SIGNAL("currentIndexChanged(int)"),self.slotWindowText)  
#        self.connect(self.buttonComboBox,SIGNAL("currentIndexChanged(int)"),self.slotButton)  
#        self.connect(self.buttonTextComboBox,SIGNAL("currentIndexChanged(int)"),self.slotButtonText)  
#        self.connect(self.baseComboBox,SIGNAL("currentIndexChanged(int)"),self.slotBase)  
          
#        gridLayout=QGridLayout()  
#        gridLayout.addWidget(label1,0,0)  
#        gridLayout.addWidget(self.windowComboBox,0,1)  
#        gridLayout.addWidget(label2,1,0)  
#        gridLayout.addWidget(self.windowTextComboBox,1,1)  
#        gridLayout.addWidget(label3,2,0)  
#        gridLayout.addWidget(self.buttonComboBox,2,1)  
#        gridLayout.addWidget(label4,3,0)  
#        gridLayout.addWidget(self.buttonTextComboBox,3,1)  
#        gridLayout.addWidget(label5,4,0)  
#        gridLayout.addWidget(self.baseComboBox)  
  
#        self.ctrlFrame.setLayout(gridLayout)  
  
#    def fillColorList(self,comboBox):  
#        colorList=QColor.colorNames()  
          
#        for color in colorList:  
#            pix=QPixmap(QSize(70,20))  
#            pix.fill(QColor(color))  
#            comboBox.addItem(QIcon(pix),color)  
#            comboBox.setIconSize(QSize(70,20))  
#            comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)  
          
#    def createContentFrame(self):  
#        label1=QLabel(self.tr("请选择一个值"))  
#        valueComboBox=QComboBox()  
#        valueComboBox.addItem("1")  
#        valueComboBox.addItem("2")  
#        label2=QLabel(self.tr("请输入字符串"))  
#        stringLineEdit=QLineEdit()  
#        textEditText=QTextEdit(self.tr("请输入"))  
#        hLayout=QHBoxLayout()  
#        okButton=QPushButton(self.tr("确定"))  
#        cancelButton=QPushButton(self.tr("取消"))  
#        hLayout.addStretch()  
#        hLayout.addWidget(okButton)  
#        hLayout.addWidget(cancelButton)  
#        gridLayout=QGridLayout()  
#        gridLayout.addWidget(label1,0,0)  
#        gridLayout.addWidget(valueComboBox,0,1)  
#        gridLayout.addWidget(label2,1,0)  
#        gridLayout.addWidget(stringLineEdit,1,1)  
#        gridLayout.addWidget(textEditText,2,0,1,2)  
#        gridLayout.addLayout(hLayout,3,0,1,2)  
#        self.contentFrame.setLayout(gridLayout)  
  
#    def slotWindow(self):  
#        colorList=QColor.colorNames()  
#        color=QColor(colorList[self.windowComboBox.currentIndex()])  
#        p=self.contentFrame.palette()  
#        p.setColor(QPalette.Window,color)  
#        self.contentFrame.setPalette(p)  
  
#    def slotWindowText(self):  
#        colorList=QColor.colorNames()  
#        color=QColor(colorList[self.windowComboBox.currentIndex()])  
#        p=self.contentFrame.palette()  
#        p.setColor(QPalette.WindowText,color)  
#        self.contentFrame.setPalette(p)  
  
#    def slotButton(self):  
#        colorList=QColor.colorNames()  
#        color=QColor(colorList[self.windowComboBox.currentIndex()])  
#        p=self.contentFrame.palette()  
#        p.setColor(QPalette.Button,color)  
#        self.contentFrame.setPalette(p)  
  
#    def slotButtonText(self):  
#        colorList=QColor.colorNames()  
#        color=QColor(colorList[self.windowComboBox.currentIndex()])  
#        p=self.contentFrame.palette()  
#        p.setColor(QPalette.ButtonText,color)  
#        self.contentFrame.setPalette(p)  
  
#    def slotBase(self):  
#        colorList=QColor.colorNames()  
#        color=QColor(colorList[self.windowComboBox.currentIndex()])  
#        p=self.contentFrame.palette()  
#        p.setColor(QPalette.Base,color)  
#        self.contentFrame.setPalette(p)  
 

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
        self.setMenuBar(menubar)


        # 整体布局器
        widget = QWidget()
        self.setCentralWidget(widget)

        ## 主要布局
        mainLayout=QVBoxLayout()  

        ### 表格
        table = QTableWidget(4,3)   
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)
        table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        table.resizeRowsToContents()
        table.setShowGrid(False)
        table.setAutoFillBackground(True)
        table.setFont(QFont("song",15))

        p = table.palette()
        p.setColor(QPalette.Text,QColor(255,255,255))
        p.setColor(QPalette.Base,QColor(34,34,34))
        table.setPalette(p)

      

        newItem = QTableWidgetItem(u"松鼠")  
        table.setItem(0, 0, newItem)  
          
        newItem = QTableWidgetItem(u"10cm")  
        table.setItem(0, 1, newItem)  
          
        newItem = QTableWidgetItem(u"60g")  
        table.setItem(0, 2, newItem)   
        ## 主布局添加
        mainLayout.addWidget(table) 

        # 整体布局器加入   
        widget.setLayout(mainLayout) 


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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()

    app.exec_()