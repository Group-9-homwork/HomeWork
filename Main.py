import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QHeaderView
from Spider import Ui_MainWindow as SpiderWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    spider = SpiderWindow()
    spider.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

