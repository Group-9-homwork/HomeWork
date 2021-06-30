import csv
import os
import unittest

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import code.Manage
import code.MainUI

class TestManage(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.ui = code.MainUI.Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)

        self.manage = code.Manage.ManageModule(self.ui)
        self.manage.manageStart()

    # 保存
    def testSaveFile(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        # 删除一个值
        self.ui.remark_lW_list_2.selectRow(2)
        self.manage.commentDelete()
        self.manage.commentSave()
        # 读入文件做比较
        content = pd.read_csv(os.path.realpath('data33.csv').replace("\\", "/"))
        self.assertEqual(content.iloc[2]['是否与股票相关'], "待标注")
        # 还原
        self.ui.remark_lW_list_2.selectRow(2)
        self.ui.remark_cB_class_2.setCurrentIndex(0)
        self.ui.remark_lW_label_2.setCurrentRow(0)
        self.manage.yes_click()

    # 选择上一个评论
    def testPreComment(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        self.ui.remark_lW_list_2.selectRow(3)
        self.manage.load_previous_remark()
        self.assertEqual(self.ui.remark_lW_message_2.toPlainText(), "绝味食品，泰格医药，药明康德，安图生物。新产业，逢低吸")

    # 选择下一个评论
    def testNextComment(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        self.ui.remark_lW_list_2.selectRow(2)
        self.manage.load_next_remark()
        self.assertEqual(self.ui.remark_lW_message_2.toPlainText(), "绝味食品今天要创反弹以来的收盘最高价，68一路上来！并再次形成买点。")

    # 删除
    def testDelComment(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        self.ui.remark_lW_list_2.selectRow(2)
        self.manage.commentDelete()
        self.assertEqual(self.ui.remark_lW_list_2.item(2, 3).text(), "待标注")

    # 标注
    def testRemComment(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        self.ui.remark_lW_list_2.selectRow(2)
        self.ui.remark_cB_class_2.setCurrentIndex(0)
        self.ui.remark_lW_label_2.setCurrentRow(0)
        self.manage.yes_click()
        self.assertEqual(self.ui.remark_lW_list_2.item(2, 3).text(), "与股票相关")

    # 冲突标识
    '''def test_commentContrast(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        self.ui.remark_lW_list_2.item(1, 1).textColor()'''

    # 显示当前评论
    def testItemClick(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        # QtTest.QTest.mouseClick(self.ui.remark_lW_list_2.item(7, 0), QtCore.Qt.LeftButton)
        self.ui.remark_lW_list_2.selectRow(7)
        self.manage.item_click()
        self.assertEqual(self.ui.remark_lW_message_2.toPlainText(), " 有止跌趋势 该反弹了 加仓起")

    # 表格初始化
    def testInitTable(self):
        self.manage.TableInit()
        # QtTest.QTest.mouseClick(self.ui.remark_pB_save_2, QtCore.Qt.LeftButton)
        self.assertEqual(self.ui.remark_lW_list_2.horizontalHeaderItem(0).text(), "评论")
        self.assertEqual(self.ui.remark_lW_list_2.horizontalHeaderItem(1).text(), "文件1")
        self.assertEqual(self.ui.remark_lW_list_2.horizontalHeaderItem(2).text(), "文件2")
        self.assertEqual(self.ui.remark_lW_list_2.horizontalHeaderItem(3).text(), "是否与股票相关")

    # 评论初始化
    def testInitComment(self):
        self.ui.remark_lE_path_3.setText(os.path.realpath('data11.csv').replace("\\", "/"))
        self.ui.remark_lE_path_4.setText(os.path.realpath('data22.csv').replace("\\", "/"))
        self.ui.remark_lE_path_2.setText(os.path.realpath('data33.csv').replace("\\", "/"))
        self.manage.commentInit()
        self.assertEqual(self.ui.remark_lW_list_2.item(7, 0).text(), " 有止跌趋势 该反弹了 加仓起")
        self.assertEqual(self.ui.remark_lW_list_2.item(7, 1).text(), "与股票相关")
        self.assertEqual(self.ui.remark_lW_list_2.item(7, 2).text(), "与股票无关")
        self.assertEqual(self.ui.remark_lW_list_2.item(7, 3).text(), "与股票相关")

    # 标签初始化
    def testInitLabel(self):
        self.manage.initLabel()
        # QtTest.QTest.mouseClick(self.ui.remark_cB_class_2, QtCore.Qt.LeftButton)
        self.ui.remark_cB_class_2.setCurrentIndex(1)
        self.assertEqual(self.ui.remark_cB_class_2.currentText(), "评论类型")

    # 更新标签显示列表
    def testLabelList(self):
        # QtTest.QTest.mouseClick(self.ui.remark_cB_class_2, QtCore.Qt.LeftButton)
        self.ui.remark_cB_class_2.setCurrentIndex(1)
        self.manage.comboBox_label_choose()
        self.ui.remark_lW_label_2.setCurrentRow(1)
        self.assertEqual(self.ui.remark_lW_label_2.currentItem().text(), "中性")

    # 打开文件
    def testOpenFile(self):
        # QtTest.QTest.mouseClick(self.ui.remark_pB_open_3, QtCore.Qt.LeftButton)
        FilePath = os.path.realpath('data11.csv').replace("\\", "/")
        self.ui.remark_lE_path_3.setText(FilePath)
        self.assertEqual(self.ui.remark_lE_path_3.text(), FilePath)

if __name__ == '__main__':
    unittest.main()