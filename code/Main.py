import sys
import MainUI
from MainUI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from Spider import SpiderModule
from Label import LabelModule
from Remark import RemarkModule
from Analyze import AnalyzeModule
import GlobalValues as gv
from Manage import ManageModule


if __name__ == '__main__':
    # UI界面
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    gv._init()  # 全局变量初始化，股票代码，数据文件路径
    # 爬虫模块
    spider = SpiderModule(ui)
    spider.spiderStart()
    # 标签模块
    label = LabelModule(ui)
    label.labelStart()
    # 标注模块
    remark = RemarkModule(ui)
    remark.remarkStart()
    # 分析模块
    analyze = AnalyzeModule(ui)
    analyze.analyzeStart()
    #管理模块
    manage = ManageModule(ui)
    manage.manageStart()

    sys.exit(app.exec_())