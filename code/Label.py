import requests
import re
import time
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QWidget
from PyQt5 import Qt

from File import FileIO


class LabelModule():
    def __init__(self, ui):
        self.ui = ui
        self.LabelClassDict = {}
        # self.spiderStart()

    def labelStart(self):
        # 添加信号和槽。
        self.ui.lab_pB_addClass.clicked.connect(self.labelClassAdd)
        self.ui.lab_pB_delClass.clicked.connect(self.labelClassDel)
        self.ui.lab_lW_ClassMessage.itemDoubleClicked.connect(self.labelClassModify)

        self.ui.lab_pB_addLabel.clicked.connect(self.labelAdd)
        self.ui.lab_pB_delLabel.clicked.connect(self.labelDel)


    def labelClassAdd(self):
        ex = App()
        labelClassName = ex.getText()
        self.ui.lab_lW_ClassMessage.addItem(labelClassName)

    def labelClassDel(self):
        # self.ui.lab_lW_ClassMessage.takeItem('byhy')
        item = self.ui.lab_lW_ClassMessage.currentItem()
        self.ui.lab_lW_ClassMessage.takeItem(self.ui.lab_lW_ClassMessage.row(item))

    def labelClassModify(self):
        # print(item)
        item = self.ui.lab_lW_ClassMessage.currentItem()
        num = self.ui.lab_lW_ClassMessage.row(item)

        ex = App()
        labelClassName = ex.getText()
        self.ui.lab_lW_ClassMessage.takeItem(num)
        self.ui.lab_lW_ClassMessage.insertItem(num, labelClassName)

        # self.ui.lab_lW_ClassMessage.currentRowChanged("222")
        # self.listWidget.itemChanged.connect(lambda: ChangeItem(item))


    def labelAdd(self):
        pass

    def labelDel(self):
        pass

    def labelModify(self):
        pass


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 540
        self.top = 250
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def getText(self):
        # self.show()
        text, okPressed = QInputDialog.getText(self, "添加标签类","请输入标签类名:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
        return text

