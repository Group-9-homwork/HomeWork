import codecs
import json
from tkinter import *
import tkinter.filedialog
import csv
import pandas as pd
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QColor
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


class ManageModule:
    def __init__(self, ui):
        self.ui = ui
        self.dfFile = pd.DataFrame()  # 两个文件相同的数据
        self.dfFileTmp = pd.DataFrame()  # 第三个文件不同的数据
        self.ui.remark_lE_path_3.setReadOnly(True)
        self.ui.remark_lE_path_4.setReadOnly(True)
        self.ui.remark_lE_path_2.setReadOnly(True)
        self.fileIO = FileIO()
        # self.filePath = file_path
        self.LabelClassDict = {}
        self.time = {}
        self.columns = {}
        self.getLabel()
        self.load_label_ComboBox()
        self.comboBox_label_choose()

        # print(self.LabelClassDict)

    def manageStart(self):
        # 文件槽
        self.ui.remark_pB_open_3.clicked.connect(self.openFile1)  # 文件1
        self.ui.remark_pB_open_4.clicked.connect(self.openFile2)  # 文件2
        self.ui.remark_pB_open_2.clicked.connect(self.openFile3)  # 保存的文件
        self.ui.remark_pB_save_2.clicked.connect(self.commentInit)  # 初始化表格

        self.ui.remark_cB_class_2.currentIndexChanged.connect(self.comboBox_label_choose)

        self.ui.tabWidget.currentChanged.connect(self.initLabel)  # 绑定TAB标签点击时的信号与槽函数

        #self.ui.ann_pB_pre_3.clicked.connect(self.load_previous_remark)  # 绑定上一个按钮
        #self.ui.ann_pB_pre_2.clicked.connect(self.load_next_remark)  # 绑定下一个按钮
        self.ui.ann_pB_next_2.clicked.connect(self.commentDelete)  # 绑定删除按钮
        self.ui.remark_lW_list_2.itemClicked.connect(self.item_click)  # 绑定列表点击
        self.ui.ann_pB_yes_2.clicked.connect(self.yes_click)  # 绑定列表点击
        self.ui.remark_lW_label_2.itemClicked.connect(self.get_label_click)  # 绑定列表点击

    def TableInit(self):
        # print(list(self.LabelClassDict.keys()))
        ColumnCount = self.LabelClassDict.__len__()*3 + 1
        self.ui.remark_lW_list_2.setColumnCount(ColumnCount)
        # 设置评论
        item = QtWidgets.QTableWidgetItem()
        item.setText("评论")
        self.ui.remark_lW_list_2.setHorizontalHeaderItem(0, item)
        # 设置标签
        for i in range(0, len(self.LabelClassDict)):
            item = QtWidgets.QTableWidgetItem()
            # item.setText(list(self.LabelClassDict.keys())[i] + '1')
            item.setText('文件1')
            self.ui.remark_lW_list_2.setHorizontalHeaderItem(3*i + 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText('文件2')
            self.ui.remark_lW_list_2.setHorizontalHeaderItem(3*i + 2, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(list(self.LabelClassDict.keys())[i] )
            self.ui.remark_lW_list_2.setHorizontalHeaderItem(3*i + 3, item)

    # 文件选择获取路径，根据路径打开csv按列每行到list,list每行模板， list->csv
    def commentInit(self):

        # 判断三个路径是否全部存在且正确
        filePath1 = self.ui.remark_lE_path_3.text()  # 获取比较文件1的路径
        filePath2 = self.ui.remark_lE_path_4.text()  # 获取比较文件2的路径
        filePath = self.ui.remark_lE_path_2.text()  # 获取综合文件的路径
        # 判断文件路径是否正确
        try:
            f1 = open(filePath1)
            f1.close()
            f2 = open(filePath2)
            f2.close()
            f2 = open(filePath)
            f2.close()
        except IOError:
            return
        if not (re.search('\.csv$', filePath1) and re.search('\.csv$', filePath2) and re.search('\.csv$', filePath)):
            return

        self.TableInit()

        # 从三个文件中读取数据
        dfFile1Tmp = self.fileIO.readCsv(filePath1)  # 比较文件1的DataFrame
        dfFile2Tmp = self.fileIO.readCsv(filePath2)  # 比较文件2的DataFrame
        if dfFile1Tmp.empty or dfFile2Tmp.empty:
            QMessageBox.warning(
                None,
                '警告',
                '比较文件里没有数据！')
            return
        self.dfFileTmp = self.fileIO.readCsv(filePath)  # 综合文件的DataFrame

        # 综合三个文件的数据
        # 因为评论不可以被删除，所以有一个bug就先不管！！！
        # 文件1和文件2共有的评论抓出来，如果文件3有就一起显示，如果没有就追加
        # print(dfFile1Tmp)
        # print(dfFile2Tmp)

        dfF1AndF2 = pd.merge(dfFile1Tmp, dfFile2Tmp, on='评论')
        if dfF1AndF2.empty:
            QMessageBox.warning(
                None,
                '警告',
                '比较文件不存在可对比的数据！')
            return
        #print(dfF1AndF2)
        if self.dfFileTmp.empty:
            self.time = dfF1AndF2['时间_x'].tolist()
            dfFile1 = pd.DataFrame()
            dfFile2 = pd.DataFrame()
            dfFile = pd.DataFrame()
            dfFile1['评论'] = dfF1AndF2['评论']
            dfFile2['评论'] = dfF1AndF2['评论']
            dfFile['评论'] = dfF1AndF2['评论']
            self.dfFile['时间'] = dfF1AndF2['时间_x']
            self.dfFile['评论'] = dfF1AndF2['评论']
            for colNums in self.LabelClassDict.keys():
                dfFile1[colNums] = dfF1AndF2[colNums + '_x']
                dfFile2[colNums] = dfF1AndF2[colNums + '_y']
                dfFile[colNums] = '待标注'
                self.dfFile[colNums] = '待标注'

        else:
            self.time = dfF1AndF2['时间_x'].tolist()
            tmp = pd.merge(dfF1AndF2, self.dfFileTmp, left_on='评论', right_on='评论', how='left')
            # 把为None的改为待标注
            tmp = tmp.where(tmp.notnull(), "待标注")
            #print(tmp)
            # 拆分三个文件
            dfFile1 = pd.DataFrame()
            dfFile2 = pd.DataFrame()
            dfFile = pd.DataFrame()
            dfFile1['评论'] = tmp['评论']
            dfFile2['评论'] = tmp['评论']
            dfFile['评论'] = tmp['评论']
            self.dfFile['时间'] = dfF1AndF2['时间_x']
            self.dfFile['评论'] = dfF1AndF2['评论']
            for colNums in self.LabelClassDict.keys():
                dfFile1[colNums] = tmp[colNums + '_x']
                dfFile2[colNums] = tmp[colNums + '_y']
                dfFile[colNums] = tmp[colNums]
                self.dfFile[colNums] = tmp[colNums]

            # 把原有的评论数据重复的删除
            for rowComment in dfFile['评论'].values:
                # print(rowComment)
                ind = self.dfFileTmp[self.dfFileTmp['评论'] == rowComment].index.tolist()
                if ind != []:
                    self.dfFileTmp.drop(ind, inplace=True)

        # 显示在表格上
        # self.time = dfFile1['时间'].tolist()
        self.columns = dfFile1.columns.tolist()
        self.ui.remark_lW_list_2.setRowCount(0)
        for i in range(dfFile1.shape[0]):
            # 每一行变成列表
            comFile1 = dfFile1.iloc[i].tolist()
            comFile2 = dfFile2.iloc[i].tolist()
            comFile = dfFile.iloc[i].tolist()
            # print(new_comment)

            curRow = self.ui.remark_lW_list_2.rowCount()  # 获得当前行
            self.ui.remark_lW_list_2.insertRow(curRow)  # 插入新行

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
        self.commentSave()

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
                elif comment1 != comment2:
                    if self.ui.remark_lW_list_2.item(row, column).text() == '冲突':
                        self.ui.remark_lW_list_2.item(row, column).setForeground(QBrush(QColor(255, 0, 0)))
                    else:
                        self.ui.remark_lW_list_2.item(row, column).setForeground(QBrush(QColor(0, 200,  0)))

    def initLabel(self):

        self.getLabel()
        self.ui.remark_cB_class_2.clear()
        self.load_label_ComboBox()

        self.commentInit()

    def getLabel(self):
        self.LabelClassDict = self.fileIO.readJson()

    # 读取标签类选择选项
    def load_label_ComboBox(self):
        for keys in self.LabelClassDict.keys():
            self.ui.remark_cB_class_2.addItem(keys)

    # 选择标签类时，更新标签显示列表
    def comboBox_label_choose(self):
        test_choose = self.ui.remark_cB_class_2.currentText()
        #print(test_choose)
        if test_choose != "":
            self.ui.remark_lW_label_2.clear()
            new_label = self.LabelClassDict[test_choose]
            self.ui.remark_lW_label_2.addItems(new_label)

    # 选择上一个评论
    def load_previous_remark(self):
        cur = self.ui.remark_lW_list_2.currentRow()
        #print(cur)
        if cur > 0:
            self.ui.remark_lW_message_2.setText(self.ui.remark_lW_list_2.item(cur - 1, 0).text())
            # self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur - 1, 0).text())
            self.ui.remark_lW_list_2.selectRow(cur - 1)

    # 选择下一个评论
    def load_next_remark(self):
        cur = self.ui.remark_lW_list_2.currentRow()
        total_row = self.ui.remark_lW_list_2.rowCount()
        if cur < total_row - 1:
            self.ui.remark_lW_message_2.setText(self.ui.remark_lW_list_2.item(cur + 1, 0).text())
            #self.ui.remark_lW_message.addItem(self.ui.remark_lW_list.item(cur + 1, 0).text())
            self.ui.remark_lW_list_2.selectRow(cur + 1)

    # 显示当前评论
    def item_click(self, item):
        # print (str(item.text()))
        cur = self.ui.remark_lW_list_2.currentRow()
        # self.ui.remark_lW_message.addItem(str(item.text()))
        #self.ui.remark_lW_message_2.addItem(item.text())
        self.ui.remark_lW_message_2.setText(self.ui.remark_lW_list_2.item(cur, 0).text())

    # 删除按钮
    def commentDelete(self):
        '''curRow = self.ui.remark_lW_list_2.currentRow()
        curCol = self.ui.remark_lW_list_2.currentColumn()
        self.ui.remark_lW_list_2.setItem(curRow, curCol, QTableWidgetItem("待标注"))
        # self.commentSave()'''

        # 检查评论是否选中
        curRow = self.ui.remark_lW_list_2.currentRow()
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
            test_choose = self.ui.remark_cB_class_2.currentText()
            total_column = self.ui.remark_lW_list_2.columnCount() - 1
            for i in range(total_column):
                key_list.append(self.ui.remark_lW_list_2.horizontalHeaderItem(i + 1).text())
            for cols in key_list:
                count += 1
                if test_choose == cols:
                    #print(cols)
                    self.dfFile[cols].iloc[curRow] = "待标注"
                    self.ui.remark_lW_list_2.setItem(curRow, count, QTableWidgetItem("待标注"))
                    #print(self.dfFile.iloc[curRow])
        self.commentSave()

    def yes_click(self):
        '''标注'''

        # 检查评论是否选中
        curRow = self.ui.remark_lW_list_2.currentRow()
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

        item = self.ui.remark_lW_label_2.currentItem()
        if None == item:  # 若用户没有点击item，则弹出提醒并返回
            QMessageBox.warning(
                None,
                '警告',
                '请选择标签')
            return None
        mark = item.text()

        if curRow != -1:
            test_choose = self.ui.remark_cB_class_2.currentText()
            total_column = self.ui.remark_lW_list_2.columnCount() - 1
            for i in range(total_column):
                key_list.append(self.ui.remark_lW_list_2.horizontalHeaderItem(i + 1).text())
            for cols in key_list:
                count += 1
                if test_choose == cols:
                    #print(cols)
                    self.dfFile[cols].iloc[curRow] = mark
                    self.ui.remark_lW_list_2.setItem(curRow, count, QTableWidgetItem(mark))
                    self.ui.remark_lW_list_2.item(curRow, count).setForeground(QBrush(QColor(0, 200, 0)))
                    #print(self.dfFile.iloc[curRow])
        self.commentSave()

    def commentSave(self):
        '''保存'''
        commentFilePath = self.ui.remark_lE_path_2.text()
        # self.dfFile与self.dfFileTmp合并
        newData = pd.concat([self.dfFileTmp, self.dfFile])

        # 写回文件
        newData.to_csv(commentFilePath, index=None)

        # commentFilePath = './data.csv'
        '''with codecs.open(commentFilePath, 'w+', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
            for row in range(self.ui.remark_lW_list_2.rowCount()):
                row_data = [self.time[row]]
                for column in range(self.ui.remark_lW_list_2.columnCount()):
                    if column % 3 == 0:
                        item = self.ui.remark_lW_list_2.item(row, column)
                        # rowdata.append(unicode(item.text()).encode('utf8'))
                        row_data.append(item.text())
                writer.writerow(row_data)'''
        # print("保存成功")

    def get_label_click(self, item):
        global CONSTANT
        CONSTANT = item.text()

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
