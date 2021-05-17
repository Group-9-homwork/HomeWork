import sys
import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow

from Spider import SpiderModule
from Label import LabelModule
from Remark import RemarkModule
from Analyze import AnalyzeModule
import GlobalValues as gv

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainUI.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    gv._init()
    '''stock = "SH603517"
    filePath = "./" + stock + ".csv"
    gv.set_value("stock", stock)
    gv.set_value("filePath", filePath)'''

    spider = SpiderModule(ui)
    spider.spiderStart()

    label = LabelModule(ui)
    label.labelStart()

    remark = RemarkModule(ui, "./test_data.json")
    remark.remarkStart()

    analyze = AnalyzeModule(ui)
    analyze.analyzeStart()

    sys.exit(app.exec_())
