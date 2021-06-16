import json
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QWidget, QApplication
from codee.File import FileIO
import os

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QHBoxLayout, QGridLayout, QVBoxLayout, QFormLayout
from matplotlib.figure import Figure
import pandas as pd
import codee.GlobalValues as gv
from PyQt5.QtWidgets import QFileDialog
matplotlib.use("Qt5Agg")


class AnalyzeModule():
    def __init__(self, ui):
        self.ui = ui
        self.jsonIO = FileIO()
        self.initData()
        # 画图窗口初始化
        self.myF = myFigure(width=3, height=2, dpi=100)
        self.ui.ana_hL_7.addWidget(self.myF)
        # 初始化的画图
        self.chooseClass()
        # self.figure = plt.figure()
        # self.canvas = FigureCanvas(self.figure)
        # self.ui.ana_hL_5.addWidget(self.canvas)

    def initData(self):
        '''初始化数据'''
        # 获取默认路径
        '''self.ui.ana_lE_path.setText(gv.get_value('filePath'))
        self.filePath = gv.get_value('filePath')
        print(self.filePath)'''
        self.filePath = self.ui.ana_lE_path.text()
        print(self.filePath)

        # 判断路径是否存在
        if ('' == self.filePath) or (not os.path.exists(self.filePath)):
            return

        # 读取json文件来初始化
        self.LabelClassDict = self.jsonIO.readJson()  # 存储标签类和标签的字典，‘标签类：[标签]’

        # 读取数据
        data = pd.read_csv(self.filePath)
        self.total = data.shape[0]
        self.static = {}  # 存放统计结果
        for key in self.LabelClassDict.keys():
            # print(key)
            num = dict(data[key].value_counts())  # 统计标注的标签
            # 添加没有的标签
            '''for value in self.LabelClassDict[key]:  # 每个标签
                if value not in num.keys():
                    num[value] = 0.0
                else:
                    num[value] = round(num[value] / total, 2)
            num["待标注"] = round(num["待标注"] / total, 2)'''
            for value in self.LabelClassDict[key]:  # 每个标签
                if value not in num.keys():
                    num[value] = 0
            # 添加到大字典中
            self.static[key] = num

        # 清除下拉框的数据
        self.ui.ana_cB_class.clear()

        # 下拉框控件的初始化
        for keys in self.LabelClassDict.keys():
            self.ui.ana_cB_class.addItem(keys)

    def analyzeStart(self):
        '''添加信号和槽'''
        self.ui.ana_cB_class.currentIndexChanged.connect(self.chooseClass)
        self.ui.tabWidget.currentChanged.connect(self.initData)   # 绑定标签点击时的信号与槽函数
        self.ui.ana_pB_yes.clicked.connect(self.initData)
        self.ui.ana_pB_open.clicked.connect(self.openFile)

    def openFile(self):
        self.filePath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "打开文件",  # 标题
            "./",  # 起始目录
            "文件类型 (*.csv)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.ana_lE_path.setText(self.filePath)

    def chooseClass(self):
        '''根据标签类画图'''
        # 画图
        plt.rcParams['font.sans-serif'] = ['simhei']  # 这里是matplotlib支持中文标签的方法
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示错误的问题

        self.myF.axes.cla()  # 清除图形

        # 初始化参数
        testChoose = self.ui.ana_cB_class.currentText()
        if '' == testChoose:
            return None
        print('当前标签类是：' + testChoose)
        labels = list(self.static[testChoose].keys())
        sizes = list(self.static[testChoose].values())
        explodes = [0.1 for _ in range(len(labels))]
        self.myF.axes.set_title('标签类：' + testChoose)  # 设置标题

        self.myF.axes.pie(sizes, explode=explodes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)  # 画饼图，（占比数值，偏离值，标签）
        self.myF.draw()  # 开始画图

        # 显示详细的统计数据
        self.ui.ana_tB_static.clear()
        self.ui.ana_tB_static.append('标签类名：' + testChoose +'\n')
        self.ui.ana_tB_static.append('评论总数：' + str(self.total) + '条\n')
        self.ui.ana_tB_static.append('标注情况：' + '\n')
        for label in self.static[testChoose].keys():
            self.ui.ana_tB_static.append('  ' + '\'' + label + '\'' + '总数：' + str(self.static[testChoose][label]) + '条\n')
        self.ui.cursor = self.ui.ana_tB_static.textCursor()
        self.ui.ana_tB_static.moveCursor(self.ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        self.ui.ana_tB_static.ensureCursorVisible()


# 作图类
class myFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(myFigure,self).__init__(self.fig) # 此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        # 隐藏坐标轴
        self.axes.get_yaxis().set_visible(False)
        self.axes.get_xaxis().set_visible(False)
        # 隐藏边框
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)