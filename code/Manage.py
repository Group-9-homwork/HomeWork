import codecs
import json
from tkinter import *
import tkinter.filedialog
import csv
import pandas as pd
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor

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


class ManageModule:
    def __init__(self, ui, file_path):
        self.ui = ui
        self.filePath = file_path
        self.LabelClassDict = {}
        self.time = {}
        self.columns = {}
        self.getLabel()
        self.load_label_ComboBox()
        self.TableInit()
        #self.ui.remark_lE_path.setText('./data.csv')
        # print(self.LabelClassDict)

    def TableInit(self):
        print(list(self.LabelClassDict.keys()))
        print(1)
        ColumnCount = self.LabelClassDict.__len__()*3 + 1
        self.ui.remark_lW_list_2.setColumnCount(ColumnCount)
        # 设置评论
        item = QtWidgets.QTableWidgetItem()
        item.setText("评论")
        self.ui.remark_lW_list_2.setHorizontalHeaderItem(0, item)
        print(2)
        # 设置标签
        for i in range(0, len(self.LabelClassDict)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(list(self.LabelClassDict.keys())[i] + '1')
            self.ui.remark_lW_list_2.setHorizontalHeaderItem(3*i + 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(list(self.LabelClassDict.keys())[i] + '2')
            self.ui.remark_lW_list_2.setHorizontalHeaderItem(3*i + 2, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(list(self.LabelClassDict.keys())[i] + '3')
            self.ui.remark_lW_list_2.setHorizontalHeaderItem(3*i + 3, item)
            print(3)

    # 文件选择获取路径，根据路径打开csv按列每行到list,list每行模板， list->csv

    def commentInit(self):
        # 判断三个路径是否全部存在且正确
        filePath1 = self.ui.remark_lE_path_3.text()  # 获取比较文件1的路径
        filePath2 = self.ui.remark_lE_path_4.text()  # 获取比较文件2的路径
        filePath = self.ui.remark_lE_path_2.text()  # 获取综合文件的路径
        '''if ~os.path.exists(filePath1) or ~os.path.exists(filePath2) or ~os.path.exists(filePath):  # 任意一个路径不存在则直接返回
            return'''

        # 从三个文件中读取数据
        dfFile1 = pd.read_csv(filePath1, encoding="utf-8")  # 比较文件1的DataFrame
        dfFile2 = pd.read_csv(filePath2, encoding="utf-8")  # 比较文件2的DataFrame
        try:
            dfFile = pd.read_csv(filePath, encoding="utf-8")  # 综合文件的DataFrame
        except pd.errors.EmptyDataError:
            dfFile = pd.DataFrame(index=dfFile1.index, columns=dfFile2.columns)

        print(dfFile1)
        print(dfFile2)
        print(dfFile)

        # 综合三个文件的数据

        # 显示在表格上
        self.time = dfFile1['时间'].tolist()
        self.columns = dfFile1.columns.tolist()
        del dfFile1['时间']
        del dfFile2['时间']
        del dfFile['时间']

        for i in range(dfFile1.shape[0]):
            # 每一行变成列表
            comFile1 = dfFile1.iloc[i].tolist()
            comFile2 = dfFile2.iloc[i].tolist()
            comFile = dfFile.iloc[i].tolist()
            # print(new_comment)

            curRow = self.ui.remark_lW_list_2.rowCount()  # 获得当前行
            self.ui.remark_lW_list_2.insertRow(curRow)  # 插入新行
            print(111)

            # 插入评论
            self.ui.remark_lW_list_2.setItem(curRow, 0, QTableWidgetItem(comFile1[0]))

            # 插入后面标签的数据
            for j in range(1, self.ui.remark_lW_list_2.columnCount()+1):
                # print(new_comment[j])
                if j < len(comFile1):
                    self.ui.remark_lW_list_2.setItem(curRow, 3*j-2, QTableWidgetItem(comFile1[j]))  # 文件1
                    self.ui.remark_lW_list_2.setItem(curRow, 3*j-1, QTableWidgetItem(comFile2[j]))  # 文件2
                    self.ui.remark_lW_list_2.setItem(curRow, 3*j, QTableWidgetItem(comFile[j]))  # 综合
                else:
                    self.ui.remark_lW_list_2.setItem(curRow, 3*j-2, QTableWidgetItem("待标注"))
                    self.ui.remark_lW_list_2.setItem(curRow, 3*j-1, QTableWidgetItem("待标注"))
                    self.ui.remark_lW_list_2.setItem(curRow, 3*j, QTableWidgetItem("待标注"))
            self.commentContrast(curRow)


    def openFile1(self):
        flag = 0
        FilePath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "打开文件",  # 标题
            "./",  # 起始目录
            "文件类型 (*.csv)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.remark_lE_path_3.setText(FilePath)

    def openFile2(self):
        flag = 0
        FilePath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "打开文件",  # 标题
            "./",  # 起始目录
            "文件类型 (*.csv)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.remark_lE_path_4.setText(FilePath)

    def openFile3(self):
        flag = 0
        FilePath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "打开文件",  # 标题
            "./",  # 起始目录
            "文件类型 (*.csv)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.remark_lE_path_2.setText(FilePath)

    def commentContrast(self, row):
        comment1 = ''
        comment2 = ''
        for column in range(self.ui.remark_lW_list_2.columnCount()):
            if column == 0:
                continue
            if column % 3 == 1:
                comment1 = self.ui.remark_lW_list_2.item(row, column).text()
            if column % 3 == 2:
                comment2 = self.ui.remark_lW_list_2.item(row, column).text()
            if column % 3 == 0:
                if self.ui.remark_lW_list_2.item(row, column).text() == '待标注':
                    if comment1 == comment2:
                        self.ui.remark_lW_list_2.setItem(row, column, QTableWidgetItem(comment1))
                    else:
                        self.ui.remark_lW_list_2.setItem(row, column, QTableWidgetItem("冲突"))
                        self.ui.remark_lW_list_2.item(row, column).setForeground(QBrush(QColor(255, 0, 0)))

    def commentSave(self):
        commentFilePath = self.ui.remark_lE_path_2.text()
        # commentFilePath = './data.csv'
        with codecs.open(commentFilePath, 'w+', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
            for row in range(self.ui.remark_lW_list_2.rowCount()):
                row_data = [self.time[row]]
                for column in range(self.ui.remark_lW_list_2.columnCount()):
                    if column % 3 == 0:
                        item = self.ui.remark_lW_list_2.item(row, column)
                        # rowdata.append(unicode(item.text()).encode('utf8'))
                        row_data.append(item.text())
                writer.writerow(row_data)
        # print("保存成功")

    def manageStart(self):
        # 文件槽
        self.ui.remark_pB_open_3.clicked.connect(self.openFile1)  # 文件1
        self.ui.remark_pB_open_4.clicked.connect(self.openFile2)  # 文件2
        self.ui.remark_pB_open_2.clicked.connect(self.openFile3)  # 保存的文件
        self.ui.remark_pB_save_2.clicked.connect(self.commentInit)  # 初始化表格

        self.ui.remark_cB_class_2.currentIndexChanged.connect(self.comboBox_label_choose)

        self.ui.tabWidget.currentChanged.connect(self.initLabel)  # 绑定TAB标签点击时的信号与槽函数

        self.ui.ann_pB_pre_3.clicked.connect(self.load_previous_remark)  # 绑定上一个按钮
        self.ui.ann_pB_pre_2.clicked.connect(self.load_next_remark)  # 绑定下一个按钮
        self.ui.ann_pB_next_2.clicked.connect(self.commentDelete)  # 绑定删除按钮
        self.ui.remark_lW_list_2.itemClicked.connect(self.item_click)  # 绑定列表点击
        self.ui.ann_pB_yes_2.clicked.connect(self.yes_click)  # 绑定列表点击
        self.ui.remark_lW_label_2.itemClicked.connect(self.get_label_click)  # 绑定列表点击

    def initLabel(self):

        self.getLabel()
        self.ui.remark_cB_class_2.clear()
        self.load_label_ComboBox()

        # self.remark_lW_list.clearContents()
        # self.remark_lW_list.setRowCount(0)
        #self.TableInit()
        #self.commentInit()

    def getLabel(self):
        self.LabelClassDict = read_json(self.filePath)

    # 读取标签类选择选项
    def load_label_ComboBox(self):
        for keys in self.LabelClassDict.keys():
            self.ui.remark_cB_class_2.addItem(keys)

    # 选择标签类时，更新标签显示列表
    def comboBox_label_choose(self):
        test_choose = self.ui.remark_cB_class_2.currentText()
        print(test_choose)
        if test_choose != "":
            self.ui.remark_lW_label_2.clear()
            new_label = self.LabelClassDict[test_choose]
            self.ui.remark_lW_label_2.addItems(new_label)

    # 删除按钮
    def commentDelete(self):
        curRow = self.ui.remark_lW_list_2.currentRow()
        curCol = self.ui.remark_lW_list_2.currentColumn()
        self.ui.remark_lW_list_2.setItem(curRow, curCol, QTableWidgetItem("待标注"))
        self.commentSave()

    # 选择上一个评论
    def load_previous_remark(self):
        cur = self.ui.remark_lW_list_2.currentRow()
        if cur > 0:
            self.ui.remark_lW_message_2.clear()
            self.ui.remark_lW_message_2.setText(self.ui.remark_lW_list_2.item(cur - 1, 0).text())
            # self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur - 1, 0).text())
            self.ui.remark_lW_list_2.selectRow(cur - 1)

    # 选择下一个评论
    def load_next_remark(self):
        cur = self.ui.remark_lW_list_2.currentRow()
        total_row = self.ui.remark_lW_list_2.rowCount()
        if cur < total_row - 1:
            self.ui.remark_lW_message_2.clear()
            self.ui.remark_lW_message_2.setText(self.ui.remark_lW_list.item(cur + 1, 0).text())
            # self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur + 1, 0).text())
            self.ui.remark_lW_list_2.selectRow(cur + 1)

    # 显示当前评论

    def item_click(self, item):
        # print (str(item.text()))
        self.ui.remark_lW_message_2.clear()
        # self.ui.remark_lW_message.addItem(str(item.text()))
        self.ui.remark_lW_message_2.setText(str(item.text()))

    def yes_click(self):
        global CONSTANT
        key_list = []
        count = 0
        # df = pd.read_csv('./data.csv', encoding='utf-8')
        mark = CONSTANT
        cur = self.ui.remark_lW_list_2.currentRow()
        if cur != -1:
            test_choose = self.ui.remark_cB_class_2.currentText()
            total_column = self.ui.remark_lW_list_2.columnCount() - 1
            for i in range(total_column):
                key_list.append(self.ui.remark_lW_list_2.horizontalHeaderItem(i + 1).text())
            for cols in key_list:
                count += 1
                if test_choose == cols:
                    self.ui.remark_lW_list_2.setItem(cur, count, QTableWidgetItem(mark))

                    # df[cols].loc[cur] = mark
                    # df.to_csv('./data.csv', encoding='utf-8')
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
