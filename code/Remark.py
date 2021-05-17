import json
from tkinter import *
import tkinter.filedialog
import csv
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QWidget, QTableWidgetItem, QFileDialog


def read_json(file_path):
    with open(file_path, 'r') as f:
        content = json.load(f)
    return content


"""def file_selector():
    root = Tk()
    filename = tkinter.filedialog.askopenfilename(title='选择一个txt文件',
                                                  filetypes=[('txt', '*.txt'), ('All Files', '*')],
                                                  initialdir=r'./')
    root.destroy()  # 和mainloop()配合可以关闭tk空白窗口
    root.mainloop()  #
    if filename == '':
        print("error")
    else:
        print("filename" + filename)"""


class RemarkModule:
    def __init__(self, ui, file_path):
        self.ui = ui
        self.LabelClassDict = {}
        self.getLabel(file_path)
        self.load_label_ComboBox()
        # print(self.LabelClassDict)

    # 文件选择获取路径，根据路径打开csv按列每行到list,list每行模板， list->csv
    def commentInit(self):
        # commentFilePath = self.ui.remark_lE_path.text()
        with open('F:/Pycharm/Group_9_v3/code/data.csv', 'r') as f:
            reader = csv.reader(f)
            for i in reader:
                new_comment = i[1][0:50]
                curRow = self.ui.remark_lW_list.rowCount()
                self.ui.remark_lW_list.insertRow(curRow)
                self.ui.remark_lW_list.setItem(curRow, 0, QTableWidgetItem(new_comment))
                self.ui.remark_lW_list.setItem(curRow, 1, QTableWidgetItem('待标注'))

    def remarkStart(self):
        # 添加信号和槽。
        self.ui.remark_cB_class.currentIndexChanged.connect(self.comboBox_label_choose)
        self.ui.remark_pB_open.clicked.connect(self.commentInit)

    def getLabel(self, file_path):
        self.LabelClassDict = read_json(file_path)

    # 读取标签类选择选项
    def load_label_ComboBox(self):
        for keys in self.LabelClassDict.keys():
            self.ui.remark_cB_class.addItem(keys)

    # 选择标签类时，更新标签显示列表
    def comboBox_label_choose(self):
        test_choose = self.ui.remark_cB_class.currentText()
        print(test_choose)
        if test_choose != "":
            self.ui.remark_lW_label.clear()
            new_label = self.LabelClassDict[test_choose]
            self.ui.remark_lW_label.addItems(new_label)