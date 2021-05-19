import csv
import unittest
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import code.Label
import code.MainUI

class TestRemark(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.ui = code.MainUI.Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)

        self.label = code.Label.LabelModule(self.ui)
        self.label.labelStart()

        self.dict = {'1': ['1', '1', '2', '4'], '3': ['111', '222', '444']}


    def testLabelClassAdd(self):
        labelClassName = '试一试'
        self.ui.lab_lW_ClassMessage.addItem(labelClassName)
        self.ui.lab_lW_ClassMessage.setCurrentRow(2)
        item = self.ui.lab_lW_ClassMessage.currentItem()
        self.assertEqual(item.text(), labelClassName)

    def testLabelClassDel(self):
        self.ui.lab_lW_ClassMessage.takeItem(1)
        num = self.ui.lab_lW_ClassMessage.count()
        self.assertEqual(num, 1)

    def testLabelClassModify(self):
        labelClassName = '试一试'
        self.ui.lab_lW_ClassMessage.takeItem(0)
        self.ui.lab_lW_ClassMessage.insertItem(0, labelClassName)
        self.ui.lab_lW_ClassMessage.setCurrentRow(0)
        item = self.ui.lab_lW_ClassMessage.currentItem()
        self.assertEqual(item.text(), labelClassName)

    def testClassConnectLabel(self):
        self.ui.lab_lW_ClassMessage.setCurrentRow(0)
        self.label.classConnectLabel()
        self.ui.Lab_lW_labelMessage.setCurrentRow(0)
        item = self.ui.Lab_lW_labelMessage.currentItem()
        self.assertEqual(item.text(), '1')

    def testLabelAdd(self):
        labelName = '试一试'
        self.ui.lab_lW_ClassMessage.setCurrentRow(0)
        self.label.classConnectLabel()
        self.ui.Lab_lW_labelMessage.addItem(labelName)
        self.ui.Lab_lW_labelMessage.setCurrentRow(4)
        item = self.ui.Lab_lW_labelMessage.currentItem()
        self.assertEqual(item.text(), labelName)

    def testLabelDel(self):
        self.ui.lab_lW_ClassMessage.setCurrentRow(0)
        self.label.classConnectLabel()
        self.ui.Lab_lW_labelMessage.takeItem(1)
        num = self.ui.Lab_lW_labelMessage.count()
        self.assertEqual(num, 3)

    def testLabelModify(self):
        labelName = '试一试'
        self.ui.lab_lW_ClassMessage.setCurrentRow(0)
        self.label.classConnectLabel()
        self.ui.Lab_lW_labelMessage.takeItem(0)
        self.ui.Lab_lW_labelMessage.insertItem(0, labelName)
        self.ui.Lab_lW_labelMessage.setCurrentRow(0)
        item = self.ui.Lab_lW_labelMessage.currentItem()
        self.assertEqual(item.text(), labelName)





if __name__ == '__main__':
    unittest.main()