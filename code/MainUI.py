# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(17, 20))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.spider = QtWidgets.QWidget()
        self.spider.setObjectName("spider")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.spider)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spi_vL_1 = QtWidgets.QVBoxLayout()
        self.spi_vL_1.setObjectName("spi_vL_1")
        self.spi_hL_2 = QtWidgets.QHBoxLayout()
        self.spi_hL_2.setContentsMargins(-1, 30, 500, -1)
        self.spi_hL_2.setObjectName("spi_hL_2")
        self.spi_vL_3 = QtWidgets.QVBoxLayout()
        self.spi_vL_3.setObjectName("spi_vL_3")
        self.spi_hL_9 = QtWidgets.QHBoxLayout()
        self.spi_hL_9.setObjectName("spi_hL_9")
        self.spi_l_stock = QtWidgets.QLabel(self.spider)
        self.spi_l_stock.setObjectName("spi_l_stock")
        self.spi_hL_9.addWidget(self.spi_l_stock)
        self.spi_lE_stock = QtWidgets.QLineEdit(self.spider)
        self.spi_lE_stock.setMinimumSize(QtCore.QSize(0, 0))
        self.spi_lE_stock.setText("")
        self.spi_lE_stock.setObjectName("spi_lE_stock")
        self.spi_hL_9.addWidget(self.spi_lE_stock)
        self.spi_vL_3.addLayout(self.spi_hL_9)
        self.spi_hL_10 = QtWidgets.QHBoxLayout()
        self.spi_hL_10.setObjectName("spi_hL_10")
        self.spi_l_path = QtWidgets.QLabel(self.spider)
        self.spi_l_path.setObjectName("spi_l_path")
        self.spi_hL_10.addWidget(self.spi_l_path)
        self.spi_lE_path = QtWidgets.QLineEdit(self.spider)
        self.spi_lE_path.setText("")
        self.spi_lE_path.setFrame(True)
        self.spi_lE_path.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.spi_lE_path.setCursorPosition(0)
        self.spi_lE_path.setDragEnabled(False)
        self.spi_lE_path.setObjectName("spi_lE_path")
        self.spi_hL_10.addWidget(self.spi_lE_path)
        self.spi_vL_3.addLayout(self.spi_hL_10)
        self.spi_hL_2.addLayout(self.spi_vL_3)
        self.spi_pB_yes = QtWidgets.QPushButton(self.spider)
        self.spi_pB_yes.setObjectName("spi_pB_yes")
        self.spi_hL_2.addWidget(self.spi_pB_yes)
        self.spi_pB_stop = QtWidgets.QPushButton(self.spider)
        self.spi_pB_stop.setObjectName("spi_pB_stop")
        self.spi_hL_2.addWidget(self.spi_pB_stop)
        self.spi_vL_1.addLayout(self.spi_hL_2)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.spi_vL_1.addItem(spacerItem)
        self.spi_l_message = QtWidgets.QLabel(self.spider)
        self.spi_l_message.setObjectName("spi_l_message")
        self.spi_vL_1.addWidget(self.spi_l_message)
        self.spi_tB_message = QtWidgets.QTextBrowser(self.spider)
        self.spi_tB_message.setObjectName("spi_tB_message")
        self.spi_vL_1.addWidget(self.spi_tB_message)
        self.horizontalLayout.addLayout(self.spi_vL_1)
        self.tabWidget.addTab(self.spider, "")
        self.label = QtWidgets.QWidget()
        self.label.setObjectName("label")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.label)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lab_hL_1 = QtWidgets.QHBoxLayout()
        self.lab_hL_1.setContentsMargins(150, 40, 150, 80)
        self.lab_hL_1.setObjectName("lab_hL_1")
        self.lab_vL_2 = QtWidgets.QVBoxLayout()
        self.lab_vL_2.setObjectName("lab_vL_2")
        self.lab_l_class = QtWidgets.QLabel(self.label)
        self.lab_l_class.setObjectName("lab_l_class")
        self.lab_vL_2.addWidget(self.lab_l_class)
        self.lab_lW_ClassMessage = QtWidgets.QListWidget(self.label)
        self.lab_lW_ClassMessage.setObjectName("lab_lW_ClassMessage")
        self.lab_vL_2.addWidget(self.lab_lW_ClassMessage)
        self.lab_hL_4 = QtWidgets.QHBoxLayout()
        self.lab_hL_4.setObjectName("lab_hL_4")
        self.lab_pB_addClass = QtWidgets.QPushButton(self.label)
        self.lab_pB_addClass.setObjectName("lab_pB_addClass")
        self.lab_hL_4.addWidget(self.lab_pB_addClass)
        self.lab_pB_delClass = QtWidgets.QPushButton(self.label)
        self.lab_pB_delClass.setObjectName("lab_pB_delClass")
        self.lab_hL_4.addWidget(self.lab_pB_delClass)
        self.lab_vL_2.addLayout(self.lab_hL_4)
        self.lab_hL_1.addLayout(self.lab_vL_2)
        spacerItem1 = QtWidgets.QSpacerItem(119, 21, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.lab_hL_1.addItem(spacerItem1)
        self.lab_vL_3 = QtWidgets.QVBoxLayout()
        self.lab_vL_3.setObjectName("lab_vL_3")
        self.lab_l_label = QtWidgets.QLabel(self.label)
        self.lab_l_label.setObjectName("lab_l_label")
        self.lab_vL_3.addWidget(self.lab_l_label)
        self.Lab_lW_labelMessage = QtWidgets.QListWidget(self.label)
        self.Lab_lW_labelMessage.setObjectName("Lab_lW_labelMessage")
        self.lab_vL_3.addWidget(self.Lab_lW_labelMessage)
        self.lab_hL_5 = QtWidgets.QHBoxLayout()
        self.lab_hL_5.setObjectName("lab_hL_5")
        self.lab_pB_addLabel = QtWidgets.QPushButton(self.label)
        self.lab_pB_addLabel.setObjectName("lab_pB_addLabel")
        self.lab_hL_5.addWidget(self.lab_pB_addLabel)
        self.lab_pB_delLabel = QtWidgets.QPushButton(self.label)
        self.lab_pB_delLabel.setObjectName("lab_pB_delLabel")
        self.lab_hL_5.addWidget(self.lab_pB_delLabel)
        self.lab_vL_3.addLayout(self.lab_hL_5)
        self.lab_hL_1.addLayout(self.lab_vL_3)
        self.horizontalLayout_6.addLayout(self.lab_hL_1)
        self.tabWidget.addTab(self.label, "")
        self.annotation = QtWidgets.QWidget()
        self.annotation.setObjectName("annotation")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.annotation)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.ann_vL_1 = QtWidgets.QVBoxLayout()
        self.ann_vL_1.setObjectName("ann_vL_1")
        self.ann_hL_2 = QtWidgets.QHBoxLayout()
        self.ann_hL_2.setContentsMargins(-1, -1, 700, -1)
        self.ann_hL_2.setObjectName("ann_hL_2")
        self.ann_l_path = QtWidgets.QLabel(self.annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ann_l_path.sizePolicy().hasHeightForWidth())
        self.ann_l_path.setSizePolicy(sizePolicy)
        self.ann_l_path.setMinimumSize(QtCore.QSize(89, 0))
        self.ann_l_path.setObjectName("ann_l_path")
        self.ann_hL_2.addWidget(self.ann_l_path)
        self.remark_lE_path = QtWidgets.QLineEdit(self.annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remark_lE_path.sizePolicy().hasHeightForWidth())
        self.remark_lE_path.setSizePolicy(sizePolicy)
        self.remark_lE_path.setMinimumSize(QtCore.QSize(250, 0))
        self.remark_lE_path.setObjectName("remark_lE_path")
        self.ann_hL_2.addWidget(self.remark_lE_path)
        self.remark_pB_open = QtWidgets.QPushButton(self.annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remark_pB_open.sizePolicy().hasHeightForWidth())
        self.remark_pB_open.setSizePolicy(sizePolicy)
        self.remark_pB_open.setMinimumSize(QtCore.QSize(0, 0))
        self.remark_pB_open.setObjectName("remark_pB_open")
        self.ann_hL_2.addWidget(self.remark_pB_open)
        self.ann_vL_1.addLayout(self.ann_hL_2)
        self.ann_hL_3 = QtWidgets.QHBoxLayout()
        self.ann_hL_3.setContentsMargins(-1, -1, 815, -1)
        self.ann_hL_3.setObjectName("ann_hL_3")
        self.ann_l_class = QtWidgets.QLabel(self.annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ann_l_class.sizePolicy().hasHeightForWidth())
        self.ann_l_class.setSizePolicy(sizePolicy)
        self.ann_l_class.setMinimumSize(QtCore.QSize(90, 0))
        self.ann_l_class.setObjectName("ann_l_class")
        self.ann_hL_3.addWidget(self.ann_l_class)
        self.remark_cB_class = QtWidgets.QComboBox(self.annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remark_cB_class.sizePolicy().hasHeightForWidth())
        self.remark_cB_class.setSizePolicy(sizePolicy)
        self.remark_cB_class.setMinimumSize(QtCore.QSize(250, 0))
        self.remark_cB_class.setObjectName("remark_cB_class")
        self.ann_hL_3.addWidget(self.remark_cB_class)
        self.ann_vL_1.addLayout(self.ann_hL_3)
        self.ann_hL_4 = QtWidgets.QHBoxLayout()
        self.ann_hL_4.setObjectName("ann_hL_4")
        self.remark_lW_label = QtWidgets.QListWidget(self.annotation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remark_lW_label.sizePolicy().hasHeightForWidth())
        self.remark_lW_label.setSizePolicy(sizePolicy)
        self.remark_lW_label.setMinimumSize(QtCore.QSize(0, 0))
        self.remark_lW_label.setObjectName("remark_lW_label")
        self.ann_hL_4.addWidget(self.remark_lW_label)
        self.ann_vL_5 = QtWidgets.QVBoxLayout()
        self.ann_vL_5.setObjectName("ann_vL_5")
        self.remark_lW_message = QtWidgets.QListWidget(self.annotation)
        self.remark_lW_message.setObjectName("remark_lW_message")
        self.ann_vL_5.addWidget(self.remark_lW_message)
        self.ann_hL_6 = QtWidgets.QHBoxLayout()
        self.ann_hL_6.setObjectName("ann_hL_6")
        self.ann_pB_pre = QtWidgets.QPushButton(self.annotation)
        self.ann_pB_pre.setObjectName("ann_pB_pre")
        self.ann_hL_6.addWidget(self.ann_pB_pre)
        self.ann_pB_yes = QtWidgets.QPushButton(self.annotation)
        self.ann_pB_yes.setObjectName("ann_pB_yes")
        self.ann_hL_6.addWidget(self.ann_pB_yes)
        self.ann_pB_next = QtWidgets.QPushButton(self.annotation)
        self.ann_pB_next.setObjectName("ann_pB_next")
        self.ann_hL_6.addWidget(self.ann_pB_next)
        self.ann_vL_5.addLayout(self.ann_hL_6)
        self.remark_lW_list = QtWidgets.QListWidget(self.annotation)
        self.remark_lW_list.setObjectName("remark_lW_list")
        self.ann_vL_5.addWidget(self.remark_lW_list)
        self.ann_hL_4.addLayout(self.ann_vL_5)
        self.ann_vL_1.addLayout(self.ann_hL_4)
        self.horizontalLayout_14.addLayout(self.ann_vL_1)
        self.tabWidget.addTab(self.annotation, "")
        self.analyze = QtWidgets.QWidget()
        self.analyze.setObjectName("analyze")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.analyze)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.ana_vL_2 = QtWidgets.QVBoxLayout()
        self.ana_vL_2.setContentsMargins(-1, -1, -1, 20)
        self.ana_vL_2.setObjectName("ana_vL_2")
        self.ana_hL_3 = QtWidgets.QHBoxLayout()
        self.ana_hL_3.setContentsMargins(-1, -1, 700, -1)
        self.ana_hL_3.setObjectName("ana_hL_3")
        self.ana_l_open = QtWidgets.QLabel(self.analyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ana_l_open.sizePolicy().hasHeightForWidth())
        self.ana_l_open.setSizePolicy(sizePolicy)
        self.ana_l_open.setMinimumSize(QtCore.QSize(89, 0))
        self.ana_l_open.setObjectName("ana_l_open")
        self.ana_hL_3.addWidget(self.ana_l_open)
        self.ana_lE_path = QtWidgets.QLineEdit(self.analyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ana_lE_path.sizePolicy().hasHeightForWidth())
        self.ana_lE_path.setSizePolicy(sizePolicy)
        self.ana_lE_path.setMinimumSize(QtCore.QSize(250, 0))
        self.ana_lE_path.setObjectName("ana_lE_path")
        self.ana_hL_3.addWidget(self.ana_lE_path)
        self.ana_pB_open = QtWidgets.QPushButton(self.analyze)
        self.ana_pB_open.setObjectName("ana_pB_open")
        self.ana_hL_3.addWidget(self.ana_pB_open)
        self.ana_vL_2.addLayout(self.ana_hL_3)
        self.ana_hL_4 = QtWidgets.QHBoxLayout()
        self.ana_hL_4.setContentsMargins(-1, -1, 816, -1)
        self.ana_hL_4.setObjectName("ana_hL_4")
        self.ana_l_class = QtWidgets.QLabel(self.analyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ana_l_class.sizePolicy().hasHeightForWidth())
        self.ana_l_class.setSizePolicy(sizePolicy)
        self.ana_l_class.setMinimumSize(QtCore.QSize(90, 0))
        self.ana_l_class.setObjectName("ana_l_class")
        self.ana_hL_4.addWidget(self.ana_l_class)
        self.ana_cB_class = QtWidgets.QComboBox(self.analyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ana_cB_class.sizePolicy().hasHeightForWidth())
        self.ana_cB_class.setSizePolicy(sizePolicy)
        self.ana_cB_class.setMinimumSize(QtCore.QSize(250, 0))
        self.ana_cB_class.setObjectName("ana_cB_class")
        self.ana_hL_4.addWidget(self.ana_cB_class)
        self.ana_vL_2.addLayout(self.ana_hL_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.ana_vL_2.addItem(spacerItem2)
        self.ana_hL_5 = QtWidgets.QHBoxLayout()
        self.ana_hL_5.setContentsMargins(160, 0, 160, -1)
        self.ana_hL_5.setObjectName("ana_hL_5")
        self.ana_hL_7 = QtWidgets.QHBoxLayout()
        self.ana_hL_7.setSpacing(27)
        self.ana_hL_7.setObjectName("ana_hL_7")
        self.widget = QtWidgets.QWidget(self.analyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.ana_hL_7.addWidget(self.widget)
        self.ana_hL_5.addLayout(self.ana_hL_7)
        self.ana_tB_static = QtWidgets.QTextBrowser(self.analyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ana_tB_static.sizePolicy().hasHeightForWidth())
        self.ana_tB_static.setSizePolicy(sizePolicy)
        self.ana_tB_static.setObjectName("ana_tB_static")
        self.ana_hL_5.addWidget(self.ana_tB_static)
        self.ana_vL_2.addLayout(self.ana_hL_5)
        self.horizontalLayout_34.addLayout(self.ana_vL_2)
        self.tabWidget.addTab(self.analyze, "")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.tabWidget.addTab(self.about, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据标注软件"))
        self.spi_l_stock.setText(_translate("MainWindow", "股票代号："))
        self.spi_lE_stock.setPlaceholderText(_translate("MainWindow", "例如：SH603517"))
        self.spi_l_path.setText(_translate("MainWindow", "保存路径："))
        self.spi_lE_path.setPlaceholderText(_translate("MainWindow", "例如：D:/data/data.csv"))
        self.spi_pB_yes.setText(_translate("MainWindow", "开始"))
        self.spi_pB_stop.setText(_translate("MainWindow", "暂停"))
        self.spi_l_message.setText(_translate("MainWindow", "爬取信息："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spider), _translate("MainWindow", "爬虫"))
        self.lab_l_class.setText(_translate("MainWindow", "标签类"))
        self.lab_pB_addClass.setText(_translate("MainWindow", "添加标签类"))
        self.lab_pB_delClass.setText(_translate("MainWindow", "删除标签类"))
        self.lab_l_label.setText(_translate("MainWindow", "标签"))
        self.lab_pB_addLabel.setText(_translate("MainWindow", "添加标签"))
        self.lab_pB_delLabel.setText(_translate("MainWindow", "删除标签"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.label), _translate("MainWindow", "标签"))
        self.ann_l_path.setText(_translate("MainWindow", "打开路径："))
        self.remark_lE_path.setPlaceholderText(_translate("MainWindow", "例如：D:/data/data.csv"))
        self.remark_pB_open.setText(_translate("MainWindow", "打开"))
        self.ann_l_class.setText(_translate("MainWindow", "选择标签类："))
        self.ann_pB_pre.setText(_translate("MainWindow", "上一条"))
        self.ann_pB_yes.setText(_translate("MainWindow", "标注"))
        self.ann_pB_next.setText(_translate("MainWindow", "下一条"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.annotation), _translate("MainWindow", "标注"))
        self.ana_l_open.setText(_translate("MainWindow", "打开路径："))
        self.ana_lE_path.setPlaceholderText(_translate("MainWindow", "例如：D:/data/data.csv"))
        self.ana_pB_open.setText(_translate("MainWindow", "打开"))
        self.ana_l_class.setText(_translate("MainWindow", "选择标签类："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyze), _translate("MainWindow", "分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("MainWindow", "关于"))

