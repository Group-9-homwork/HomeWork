import sys
import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow

from Spider import SpiderModule
from Label import LabelModule
from Remark import RemarkModule

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainUI.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    spider = SpiderModule(ui)
    spider.spiderStart()

    label = LabelModule(ui)
    label.labelStart()

    remark = RemarkModule(ui, "./test_data.json")
    remark.remarkStart()

    '''LabelClassInit(ui)
    AnnotationInit(ui)
    AnalysisInit(ui)
    AboutInit(ui)'''

    sys.exit(app.exec_())
