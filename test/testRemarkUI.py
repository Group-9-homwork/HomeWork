import csv
import unittest

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import code.Remark
import code.MainUI

class TestRemark(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.ui = codee.MainUI.Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)

        self.remark = codee.Remark.RemarkModule(self.ui, "./test_data.json")
        self.remark.remarkStart()
        self.remark.commentInit()

    # 测试标签类读取
    def test_ComboBox(self):#remark_cB_class
        QtTest.QTest.mouseClick(self.ui.remark_cB_class,QtCore.Qt.LeftButton)
        self.ui.remark_cB_class.setCurrentIndex(1)
        self.assertEqual(self.ui.remark_cB_class.currentText(), "3")

    #测试标签列表
    def test_remark_lW_label(self):
        QtTest.QTest.mouseClick(self.ui.remark_cB_class, QtCore.Qt.LeftButton)
        self.ui.remark_cB_class.setCurrentIndex(1)
        self.ui.remark_lW_label.setCurrentRow(1)
        #code.Remark.RemarkModule.comboBox_label_choose(self)
        self.assertEqual(self.ui.remark_lW_label.currentItem().text(), "222")

    #测试表格初始化
    def test_TableInit(self):
        self.remark.TableInit()
        self.assertEqual(self.ui.remark_lW_list.horizontalHeaderItem(0).text(), "评论内容")
        self.assertEqual(self.ui.remark_lW_list.horizontalHeaderItem(1).text(), "1")
        self.assertEqual(self.ui.remark_lW_list.horizontalHeaderItem(2).text(), "3")

    #测试打开按钮
    def test_commentInit(self):
        QtTest.QTest.mouseClick(self.ui.remark_pB_open, QtCore.Qt.LeftButton)
        self.assertEqual(self.ui.remark_lW_list.item(0, 1).text(), "待标注")
        self.assertEqual(self.ui.remark_lW_list.item(1, 1).text(), "待标注")

    # 测试保存功能
    def test_commentSave(self):
        QtTest.QTest.mouseClick(self.ui.remark_pB_save, QtCore.Qt.LeftButton)
        self.remark.commentSave()
        commentFilePath = './data1.csv'
        df = pd.read_csv(commentFilePath, encoding="utf-8")
        columns = df.columns.tolist()
        self.assertEqual(columns[2], "1")
        self.assertEqual(columns[3], "43")



    # 测试标签读取
    def test_read_json(self):
        self.assertEqual(code.Remark.read_json("./test_data.json")['3'], ["111", "222", "444"])


if __name__ == '__main__':
    unittest.main()
