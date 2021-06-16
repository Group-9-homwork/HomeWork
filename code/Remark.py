import codecs
import json
from tkinter import *
import tkinter.filedialog
import csv
import pandas as pd
import os

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QInputDialog, QLineEdit, QWidget, QTableWidgetItem, QFileDialog,QMessageBox
from File import FileIO


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

# 表格不可点击编辑！！！！

class RemarkModule:
    def __init__(self, ui):
        self.ui = ui
        self.ui.remark_lE_path.setReadOnly(True)
        self.data = pd.DataFrame()  # dataframe数据
        self.row = -1  # 当前点击item的行
        self.col = -1  # 当前点击item的列
        self.fileIO = FileIO()
        # self.filePath = file_path
        self.LabelClassDict = {}
        self.time = {}
        self.columns = {}
        self.getLabel()
        self.load_label_ComboBox()
        self.comboBox_label_choose()
        # self.TableInit()
        # self.ui.remark_lE_path.setText('./data.csv')
        # print(self.LabelClassDict)
        self.filePath = 0

    def remarkStart(self):
        # 添加信号和槽。#将ui中的控件与自定义函数连接
        self.ui.remark_cB_class.currentIndexChanged.connect(self.comboBox_label_choose)  # 下拉框切换
        self.ui.remark_pB_save.clicked.connect(self.commentInit)  # 确认按钮
        self.ui.remark_pB_open.clicked.connect(self.openFile)  # 打开文件按钮
        self.ui.remark_pB_save2.clicked.connect(self.saveFile)  # 另存为按钮

        self.ui.tabWidget.currentChanged.connect(self.initLabel)  # 绑定TAB标签点击时的信号与槽函数

        self.ui.ann_pB_pre.clicked.connect(self.load_previous_remark)  # 绑定上一个按钮
        self.ui.ann_pB_next.clicked.connect(self.load_next_remark)  # 绑定下一个按钮
        self.ui.pushButton.clicked.connect(self.commentDelete)  # 绑定删除按钮
        self.ui.remark_lW_list.itemClicked.connect(self.item_click)  # 绑定列表点击
        self.ui.ann_pB_yes.clicked.connect(self.yes_click)  # 绑定列表点击
        self.ui.remark_lW_label.itemClicked.connect(self.get_label_click)  # 绑定列表点击


    def TableInit(self):
        '''表头初始化'''
        ColumnCount = self.LabelClassDict.__len__() + 1
        self.ui.remark_lW_list.setColumnCount(ColumnCount)

        item = QtWidgets.QTableWidgetItem()
        item.setText('评论')
        self.ui.remark_lW_list.setHorizontalHeaderItem(0, item)
        # print(list(self.LabelClassDict.keys()))
        for i in range(len(self.LabelClassDict)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(list(self.LabelClassDict.keys())[i])
            self.ui.remark_lW_list.setHorizontalHeaderItem(i + 1, item)

    # 文件选择获取路径，根据路径打开csv按列每行到list,list每行模板， list->csv
    def commentInit(self):
        self.filePath = self.ui.remark_lE_path.text()
        print(self.filePath)

        # 判断文件路径是否正确
        if not re.search('^((?:[a-zA-Z]:)?\/(?:[^\\\?\/\*\|<>:"]+\/)+)', self.filePath):
            QMessageBox.warning(
                None,
                '警告',
                '文件路径错误，请重新输入！')
            return

        if not re.search('\.csv$', self.filePath):
            QMessageBox.warning(
                None,
                '警告',
                '文件类型错误，请选择csv文件！')
            return

        '''f = open(self.filePath, 'a+')  # 如果不存在则创建一个
        f.close()'''

        self.ui.remark_lW_list.setRowCount(0)
        # df = pd.read_csv(self.filePath, encoding="utf-8")
        self.data = self.fileIO.readCsv(self.filePath)
        if self.data.empty:
            QMessageBox.warning(
                None,
                '警告',
                '该文件里没有数据！')
            return

        self.TableInit()

        self.time = self.data['时间'].tolist()
        self.columns = self.data.columns.tolist()

        # print(self.time)
        # print(self.columns)
        del self.data['时间']
        print(self.data)
        for i in range(self.data.shape[0]):
            new_comment = self.data.iloc[i].tolist()
            # print(new_comment)
            curRow = self.ui.remark_lW_list.rowCount()
            self.ui.remark_lW_list.insertRow(curRow)
            # print(111)
            for j in range(self.ui.remark_lW_list.columnCount()):
                if j < len(new_comment):
                    self.ui.remark_lW_list.setItem(curRow, j, QTableWidgetItem(new_comment[j]))
                else:
                    self.ui.remark_lW_list.setItem(curRow, j, QTableWidgetItem("待标注"))


    # 文件选择获取路径，根据路径打开csv按列每行到list,list每行模板， list->csv
    def commentInit2(self):
        self.filePath = self.ui.remark_lE_path.text()

        # 判断文件路径是否正确
        if not re.search('^((?:[a-zA-Z]:)?\/(?:[^\\\?\/\*\|<>:"]+\/)+)', self.filePath):
            return

        if not re.search('\.csv$', self.filePath):
            return

        '''f = open(self.filePath, 'a+')  # 如果不存在则创建一个
        f.close()'''

        self.ui.remark_lW_list.setRowCount(0)
        # df = pd.read_csv(self.filePath, encoding="utf-8")
        self.data = self.fileIO.readCsv(self.filePath)
        if self.data.empty:
            QMessageBox.warning(
                None,
                '警告',
                '该文件里没有数据！')
            return

        self.TableInit()

        self.time = self.data['时间'].tolist()
        self.columns = self.data.columns.tolist()

        # print(self.time)
        # print(self.columns)
        del self.data['时间']
        print(self.data)
        for i in range(self.data.shape[0]):
            new_comment = self.data.iloc[i].tolist()
            # print(new_comment)
            curRow = self.ui.remark_lW_list.rowCount()
            self.ui.remark_lW_list.insertRow(curRow)
            # print(111)
            for j in range(self.ui.remark_lW_list.columnCount()):
                if j < len(new_comment):
                    self.ui.remark_lW_list.setItem(curRow, j, QTableWidgetItem(new_comment[j]))
                else:
                    self.ui.remark_lW_list.setItem(curRow, j, QTableWidgetItem("待标注"))

    def openFile(self):
        flag = 0
        self.filePath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "打开文件",  # 标题
            "./",  # 起始目录
            "文件类型 (*.csv)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.remark_lE_path.setText(self.filePath)
        print(self.filePath)

    def saveFile(self):
        '''保存文件'''
        saveFilePath, _  = QFileDialog.getSaveFileName(None, "保存文件", self.filePath,
                                    "文件类型 (*.csv)")
        print(saveFilePath)
        # 通过pandas保存
        # 读取原有的数据
        oldData = pd.read_csv(self.filePath)
        # 将新的数据替换
        for colName in self.data.columns.values.tolist():
            oldData[colName] = self.data[colName]

        # 再写回
        oldData.to_csv(saveFilePath, index=None)


    def initLabel(self):
        self.getLabel()
        self.ui.remark_cB_class.clear()
        self.load_label_ComboBox()
        # self.remark_lW_list.clearContents()
        # self.remark_lW_list.setRowCount(0)
        # self.TableInit()
        self.commentInit2()

    def getLabel(self):
        self.LabelClassDict = self.fileIO.readJson()

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

    # 选择上一个评论
    def load_previous_remark(self):
        cur = self.ui.remark_lW_list.currentRow()
        if cur > 0:
            self.ui.remark_lW_message.setText(self.ui.remark_lW_list.item(cur - 1, 0).text())
            #self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur - 1, 0).text())
            self.ui.remark_lW_list.selectRow(cur - 1)

    # 选择下一个评论
    def load_next_remark(self):
        cur = self.ui.remark_lW_list.currentRow()
        total_row = self.ui.remark_lW_list.rowCount()
        if cur < total_row-1:
            self.ui.remark_lW_message.setText(self.ui.remark_lW_list.item(cur + 1, 0).text())
            #self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur + 1, 0).text())
            self.ui.remark_lW_list.selectRow(cur + 1)

    # 显示当前评论
    def item_click(self, item):
        # print (str(item.text()))
        cur = self.ui.remark_lW_list.currentRow()
        # self.ui.remark_lW_message.addItem(str(item.text()))
        # item = self.ui.remark_lW_list.currentItem()
        self.ui.remark_lW_message.setText(self.ui.remark_lW_list.item(cur, 0).text())

    # 删除按钮
    def commentDelete(self):
        '''curRow = self.ui.remark_lW_list.currentRow()
        curCol = self.ui.remark_lW_list.currentColumn()
        # print(curRow)
        # print(curCol)
        # 判断是否存在点击
        if curRow == -1 or curCol == -1 or curCol == 0:
            return
        # print(self.data[list(self.LabelClassDict.keys())[curCol]].iloc[curRow])
        # print(self.data.iloc[curRow])
        self.data[list(self.LabelClassDict.keys())[curCol]].iloc[curRow] = "待标注"
        self.ui.remark_lW_list.setItem(curRow, curCol, QTableWidgetItem("待标注"))
        print(self.data.iloc[curRow])
        # self.commentSave()'''

        # 检查评论是否选中
        curRow = self.ui.remark_lW_list.currentRow()
        if curRow == -1:
            QMessageBox.warning(
                None,
                '警告',
                '请选择评论！')
            return

        global CONSTANT
        key_list = []
        count = 0

        if curRow != -1:
            test_choose = self.ui.remark_cB_class.currentText()
            total_column = self.ui.remark_lW_list.columnCount() - 1
            for i in range(total_column):
                key_list.append(self.ui.remark_lW_list.horizontalHeaderItem(i + 1).text())
            for cols in key_list:
                count += 1
                if test_choose == cols:
                    print(cols)
                    self.data[cols].iloc[curRow] = "待标注"
                    self.ui.remark_lW_list.setItem(curRow, count, QTableWidgetItem("待标注"))
                    print(self.data.iloc[curRow])
        self.commentSave()

    def yes_click(self):
        '''标注'''
        # 检查评论是否选中
        curRow = self.ui.remark_lW_list.currentRow()
        if curRow == -1:
            QMessageBox.warning(
                None,
                '警告',
                '请选择评论！')
            return
        # 检查标签是否选中
        global CONSTANT
        key_list = []
        count = 0
        mark = CONSTANT

        item = self.ui.remark_lW_label.currentItem()
        if None == item:  # 若用户没有点击item，则弹出提醒并返回
            QMessageBox.warning(
                None,
                '警告',
                '请选择标签')
            return None
        mark = item.text()

        if curRow != -1:
            test_choose = self.ui.remark_cB_class.currentText()
            total_column = self.ui.remark_lW_list.columnCount() - 1
            for i in range(total_column):
                key_list.append(self.ui.remark_lW_list.horizontalHeaderItem(i + 1).text())
            for cols in key_list:
                count += 1
                if test_choose == cols:
                    print(cols)
                    self.data[cols].iloc[curRow] = mark
                    self.ui.remark_lW_list.setItem(curRow, count, QTableWidgetItem(mark))
                    print(self.data.iloc[curRow])
        self.commentSave()

    # 点击标注时保存
    def commentSave(self):
        self.filePath = self.ui.remark_lE_path.text()
        # 通过pandas保存
        # 读取原有的数据
        if not os.path.exists(self.filePath):
            oldData = pd.DataFrame()
        else:
            oldData = pd.read_csv(self.filePath)
        print(oldData)
        # 将新的数据替换
        for colName in self.data.columns.values.tolist():
            oldData[colName] = self.data[colName]

        # 再写回
        oldData.to_csv(self.filePath, index=None)

        '''self.filePath = self.ui.remark_lE_path.text()
        # self.filePath = './data.csv'
        with codecs.open(self.filePath, 'w+', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
            for row in range(self.ui.remark_lW_list.rowCount()):
                row_data = [self.time[row]]
                for column in range(self.ui.remark_lW_list.columnCount()):
                    item = self.ui.remark_lW_list.item(row, column)
                    # rowdata.append(unicode(item.text()).encode('utf8'))
                    row_data.append(item.text())
                writer.writerow(row_data)'''
        # print("保存成功")


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
