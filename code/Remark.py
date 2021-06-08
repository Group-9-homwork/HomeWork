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


CONSTANT = ""
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
        self.ui.remark_lE_path.setText('./data.csv')
        # print(self.LabelClassDict)

    def TableInit(self):

        ColumnCount = self.LabelClassDict.__len__() + 1
        self.ui.remark_lW_list.setColumnCount(ColumnCount)
        for i in range(len(self.LabelClassDict)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(list(self.LabelClassDict.keys())[i])
            self.ui.remark_lW_list.setHorizontalHeaderItem(i + 1, item)

    # 文件选择获取路径，根据路径打开csv按列每行到list,list每行模板， list->csv

    def commentInit(self):
        self.ui.remark_lW_list.setRowCount(0)
        commentFilePath = self.ui.remark_lE_path.text()
        #commentFilePath = './data.csv'
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
            for j in range(self.ui.remark_lW_list.columnCount()):

                if j < len(new_comment):
                    self.ui.remark_lW_list.setItem(curRow, j, QTableWidgetItem(new_comment[j]))
                else:
                    self.ui.remark_lW_list.setItem(curRow, j, QTableWidgetItem("待标注"))

    def openFile(self):
        flag = 0
        FilePath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "打开文件",  # 标题
            "./",  # 起始目录
            "文件类型 (*.csv)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.remark_lE_path.setText(FilePath)

    def commentSave(self):

        commentFilePath = self.ui.remark_lE_path.text()
        #commentFilePath = './data.csv'
        with codecs.open(commentFilePath, 'w+', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
            for row in range(self.ui.remark_lW_list.rowCount()):
                row_data = [self.time[row]]
                for column in range(self.ui.remark_lW_list.columnCount()):
                    item = self.ui.remark_lW_list.item(row, column)
                    # rowdata.append(unicode(item.text()).encode('utf8'))
                    row_data.append(item.text())
                writer.writerow(row_data)
        # print("保存成功")

    def remarkStart(self):
        # 添加信号和槽。#将ui中的控件与自定义函数连接
        self.ui.remark_cB_class.currentIndexChanged.connect(self.comboBox_label_choose)
        self.ui.remark_pB_open.clicked.connect(self.commentInit)
        self.ui.remark_pB_save.clicked.connect(self.openFile)

        self.ui.tabWidget.currentChanged.connect(self.initLabel)  # 绑定TAB标签点击时的信号与槽函数

        self.ui.ann_pB_pre.clicked.connect(self.load_previous_remark)  # 绑定上一个按钮
        self.ui.ann_pB_next.clicked.connect(self.load_next_remark)  # 绑定下一个按钮
        self.ui.pushButton.clicked.connect(self.commentDelete)#绑定删除按钮
        self.ui.remark_lW_list.itemClicked.connect(self.item_click)  # 绑定列表点击
        self.ui.ann_pB_yes.clicked.connect(self.yes_click)  # 绑定列表点击
        self.ui.remark_lW_label.itemClicked.connect(self.get_label_click)  # 绑定列表点击

    def initLabel(self):

        self.getLabel()
        self.ui.remark_cB_class.clear()
        self.load_label_ComboBox()

        # self.remark_lW_list.clearContents()
        # self.remark_lW_list.setRowCount(0)
        self.TableInit()
        self.commentInit()


    def getLabel(self):
        self.LabelClassDict = read_json(self.filePath)

    # 读取标签类选择选项
    def load_label_ComboBox(self):
        first=''
        self.ui.remark_cB_class.addItem(first)
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


    #删除按钮
    def commentDelete(self):
        curRow = self.ui.remark_lW_list.currentRow()
        curCol = self.ui.remark_lW_list.currentColumn()
        self.ui.remark_lW_list.setItem(curRow, curCol, QTableWidgetItem("待标注"))
        self.commentSave()

    # 选择上一个评论
    def load_previous_remark(self):
        cur = self.ui.remark_lW_list.currentRow()
        if cur > 0:
            self.ui.remark_lW_message.clear()
            self.ui.remark_lW_message.setText(self.ui.remark_lW_list.item(cur - 1, 0).text())
            #self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur - 1, 0).text())
            self.ui.remark_lW_list.selectRow(cur - 1)

    # 选择下一个评论
    def load_next_remark(self):
        cur = self.ui.remark_lW_list.currentRow()
        total_row = self.ui.remark_lW_list.rowCount()
        if cur < total_row-1:
            self.ui.remark_lW_message.clear()
            self.ui.remark_lW_message.setText(self.ui.remark_lW_list.item(cur + 1, 0).text())
            #self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur + 1, 0).text())
            self.ui.remark_lW_list.selectRow(cur + 1)

    # 显示当前评论

    def item_click(self, item):
        # print (str(item.text()))
        cur = self.ui.remark_lW_list.currentRow()
        self.ui.remark_lW_message.clear()
        #self.ui.remark_lW_message.addItem(str(item.text()))
        print(item.text)
        self.ui.remark_lW_message.setText(self.ui.remark_lW_list.item(cur, 0).text())

    def yes_click(self):
        global CONSTANT
        key_list = []
        count = 0
        #df = pd.read_csv('./data.csv', encoding='utf-8')
        mark = CONSTANT
        cur = self.ui.remark_lW_list.currentRow()
        if cur != -1:
            test_choose = self.ui.remark_cB_class.currentText()
            total_column = self.ui.remark_lW_list.columnCount() - 1
            for i in range(total_column):
                key_list.append(self.ui.remark_lW_list.horizontalHeaderItem(i + 1).text())
            for cols in key_list:
                count += 1
                if test_choose == cols:
                    self.ui.remark_lW_list.setItem(cur, count, QTableWidgetItem(mark))

                    #df[cols].loc[cur] = mark
                    #df.to_csv('./data.csv', encoding='utf-8')
        self.commentSave()

    def get_label_click(self, item):
        global CONSTANT
        CONSTANT = item.text()

# curRow 当前的列    self.ui.remark_lW_list标签的列表  insertRow(curRow) 插入行
# setItem(curRow, j, QTableWidgetItem(new_comment[j]) 设置行中的item（当前行，当前列，要添加的item）
# new_comment[j] 第一个是当前的评论 后面的是每个标签的标注状态
# setBackground()设置qtablewidgetitem的背景刷
# ann_pB_pre 上一个评论 ann_pB_yes 标注 ann_pB_next 下一个评论
# qpushbutton.click 设置点击时的反应
# remark_lW_message 上面的文本框
# remark_cB_class 标签选择项
# self.LabelClassDict.keys() 标签列表
# remark_lW_label 左侧列表
