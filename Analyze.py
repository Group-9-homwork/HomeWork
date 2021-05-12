import json
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QWidget
from File import FileIO



class AnalyzeModule():
    def __init__(self, ui):
        self.ui = ui
        self.jsonIO = FileIO()
        self.LabelClassDict = self.jsonIO.readJson()
        self.initUI()

    def initUI(self):
        for keys in self.LabelClassDict.keys():
            self.ui.ana_cB_class.addItem(keys)

    def analyzeStart(self):
        # 添加信号和槽
        self.ui.ana_cB_class.currentIndexChanged.connect(self.chooseClass)

    def chooseClass(self):
        pass