import csv
import unittest
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtTest

from PyQt5.QtWidgets import QApplication, QMainWindow


import sys

import codee.Label
import codee.MainUI

class TestRemark(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.ui = codee.MainUI.Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)

        self.label = codee.Label.LabelModule(self.ui)
        self.label.labelStart()




if __name__ == '__main__':
    unittest.main()