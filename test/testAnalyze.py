import unittest

from PyQt5 import QtTest
from PyQt5 import QtCore
from codes.Analyze import *
import sys
from codes import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyTestCase(unittest.TestCase):
    def test_initData(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        a = AnalyzeModule(ui)
        ui.ana_lE_path.setText(r'D:\test\HomeWork\test\data2.csv')
        result = a.initData(flag=0)
        self.assertEqual(result, 1)

    def test_analyzeStart(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        a = AnalyzeModule(ui)
        result = a.analyzeStart()
        self.assertEqual(result, 1)

    def test_openFile(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        a = AnalyzeModule(ui)
        result = a.openFile()
        self.assertEqual(result, 1)

    def test_chooseClass(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        a = AnalyzeModule(ui)
        a.analyzeStart()
        ui.ana_lE_path.setText(r'D:\test\HomeWork\test\data2.csv')
        QtTest.QTest.mouseClick(ui.ana_pB_yes, QtCore.Qt.LeftButton)
        QtTest.QTest.mouseClick(ui.ana_cB_class, QtCore.Qt.LeftButton)
        ui.ana_cB_class.setCurrentIndex(2)

        result = a.chooseClass()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
