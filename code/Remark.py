import codecs
import json
from tkinter import *
import tkinter.filedialog
import csv
import pandas as pd

from PyQt5 import QtWidgets

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
        self.filePath = file_path
        self.LabelClassDict = {}
        self.time = {}
        self.columns = {}
        self.getLabel()
        self.load_label_ComboBox()
        self.TableInit()

        # print(self.LabelClassDict)

    def TableInit(self):

        ColumnCount = self.LabelClassDict.__len__()+1
        self.ui.remark_lW_list.setColumnCount(ColumnCount)
        for i in range(len(self.LabelClassDict)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(list(self.LabelClassDict.keys())[i])
            self.ui.remark_lW_list.setHorizontalHeaderItem(i+1, item)

    # 文件选择获取路径，根据路径打开csv按列每行到list,list每行模板， list->csv

    def commentInit(self):
        #commentFilePath = self.ui.remark_lE_path.text()
        commentFilePath = './data.csv'
        df = pd.read_csv(commentFilePath, encoding="utf-8")
        self.time = df['时间'].tolist()
        self.columns = df.columns.tolist()
        print(self.time)
        print(self.columns)
        del df['时间']
        for i in range(df.shape[0]):
            new_comment = df.iloc[i].tolist()
            print(new_comment)

            curRow = self.ui.remark_lW_list.rowCount()
            self.ui.remark_lW_list.insertRow(curRow)
            print(111)
            for j in range(len(new_comment)):
                print(new_comment[j])
                self.ui.remark_lW_list.setItem(curRow, j, QTableWidgetItem(new_comment[j]))


        '''
        #print(df)
        n = self.LabelClassDict.__len__()
        for i in df:
            print(124)
            new_comment = i[1]
            print(new_comment)
            curRow = self.ui.remark_lW_list.rowCount()
            self.ui.remark_lW_list.insertRow(curRow)
            self.ui.remark_lW_list.setItem(curRow, 0, QTableWidgetItem(new_comment))
            for k in range(n):
                self.ui.remark_lW_list.setItem(curRow, k + 1, QTableWidgetItem('待标注'))
        
        n = self.LabelClassDict.__len__()

        print(111)
        with open(commentFilePath, 'r') as f:
            print(121)
            reader = csv.reader(f)
            print(reader)
            print(123)
            for i in reader:
                print(124)
                new_comment = i[1]
                print(new_comment)
                curRow = self.ui.remark_lW_list.rowCount()
                self.ui.remark_lW_list.insertRow(curRow)
                self.ui.remark_lW_list.setItem(curRow, 0, QTableWidgetItem(new_comment))
                for k in range(n):
                    self.ui.remark_lW_list.setItem(curRow, k+1, QTableWidgetItem('待标注'))
                    #self.ui.remark_lW_list.setItem(curRow, k + 1, QTableWidgetItem(i[k+2]))
                    #此行代码为导入csv文件中的“标注”
'''
    def commentSave(self):

        # commentFilePath = self.ui.remark_lE_path.text()
        commentFilePath = './data1.csv'
        with codecs.open(commentFilePath, 'w+', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
            for row in range(self.ui.remark_lW_list.rowCount()):
                row_data = [self.time[row]]
                for column in range(self.ui.remark_lW_list.columnCount()):
                    item = self.ui.remark_lW_list.item(row, column)
                    #rowdata.append(unicode(item.text()).encode('utf8'))
                    row_data.append(item.text())
                writer.writerow(row_data)
        #print("保存成功")

    def remarkStart(self):
        # 添加信号和槽。
        self.ui.remark_cB_class.currentIndexChanged.connect(self.comboBox_label_choose)
        self.ui.remark_pB_open.clicked.connect(self.commentInit)
        self.ui.remark_pB_save.clicked.connect(self.commentSave)

        self.ui.tabWidget.currentChanged.connect(self.initLabel)  # 绑定标签点击时的信号与槽函数

    def initLabel(self):

        self.getLabel()
        print(222)
        self.ui.remark_cB_class.clear()
        print(111)
        self.load_label_ComboBox()

    def getLabel(self):
        self.LabelClassDict = read_json(self.filePath)

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
