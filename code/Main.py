import sys
import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow

from Spider import SpiderModule
from Label import LabelModule
from Remark import RemarkModule
from Analyze import AnalyzeModule
from Manage import ManageModule

import GlobalValues as gv

if __name__ == '__main__':
    # UI界面
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainUI.Ui_MainWindow()
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
    remark = RemarkModule(ui, "./test_data.json")
    remark.remarkStart()
    # 分析模块
    analyze = AnalyzeModule(ui)
    analyze.analyzeStart()
    # 管理模块
    manage = ManageModule(ui, "./test_data.json")
    manage.manageStart()

    sys.exit(app.exec_())