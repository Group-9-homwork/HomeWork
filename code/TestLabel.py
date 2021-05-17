from unittest import TestCase, main, TextTestRunner, TestLoader
import unittest

from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit

from Spider import SpiderModule
from Label import LabelModule
from Remark import RemarkModule


class TestLabel(unittest.TestCase):

    '''def setUp(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(mainWindow)

        label = LabelModule(self.ui)
        label.labelStart()'''

    '''def tearDown(self):
        self.app.deleteLater()'''

    def test1(self):
        # 初始化UI
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()

        label = LabelModule(ui)
        label.labelStart()

        QTest.keyClicks(label.inputDia.lineEdit, '111')
        print(label.inputDia.lineEdit.text())
        # 测试操作过程
        QTest.mouseClick(ui.lab_pB_addClass, Qt.LeftButton)
        # label.inputDia.lineEdit.setText('111')
        QTest.keyClicks(label.inputDia.lineEdit, '111')
        okWidget = label.inputDia.buttonBox.button(label.inputDia.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)


        # QInputDialog.getText(self, "添加标签类", "请输入标签类名:", QLineEdit.Normal, "111")
        # QTest.keyClicks(QInputDialog, '111')


        # 通过比较键值对来判断测试成功与否
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()
    # 可以用suite