import sys
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QWidget, QMessageBox, QDialog
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from codee.File import FileIO
import codee.inputDia as inputDia
import pandas as pd
import codee.GlobalValues as gv

class LabelModule():
    def __init__(self, ui):
        self.ui = ui  # 传ui界面
        # 读取json文件来初始化
        self.jsonIO = FileIO()
        self.LabelClassDict = self.jsonIO.readJson()  # 存储标签类和标签的字典，‘标签类：[标签]’

        # 增加类和标签的输入
        self.inputDia = inputDiaClass()  # 子窗口
        # self.diaLabel = inputDiaClass()  # 标签

        # 在界面显示
        self.initUI()

    def initUI(self):
        for labelClassName in self.LabelClassDict.keys():
            self.ui.lab_lW_ClassMessage.addItem(labelClassName)  # 在listWidget添加item

        '''for index in range(self.ui.lab_lW_ClassMessage.count()):
            item = self.ui.lab_lW_ClassMessage.item(index)
            item.setFlags(item.flags() | Qt.ItemIsEditable)'''

    '''def changeDict(self):
        item = self.ui.lab_lW_ClassMessage.currentItem()  # 获取当前点击的item对象
        ind = self.ui.Lab_lW_labelMessage.row(item)
        className = item.text()
        print('1:' + className)
        return None
        # 修改字典
        # 保存字典'''

    def initData(self):
        # 读取数据
        # self.filePath = gv.get_value('filePath')
        self.filePath = './data.csv'
        self.commentData = pd.read_csv(self.filePath)
        # print(self.commentData)

    def labelStart(self):
        # 添加信号和槽。
        self.ui.lab_pB_addClass.clicked.connect(self.labelClassAdd)  # 点击添加标签类按钮
        # self.ui.lab_pB_addClass.clicked.connect(self.inputDia.show)  # 弹出对话框
        self.ui.lab_pB_delClass.clicked.connect(self.labelClassDel)  # 点击删除标签类按钮
        self.ui.lab_lW_ClassMessage.itemDoubleClicked.connect(self.labelClassModify)  # 双击标签类item
        self.ui.lab_lW_ClassMessage.itemClicked.connect(self.classConnectLabel)  # 单机标签类item

        self.ui.lab_pB_addLabel.clicked.connect(self.labelAdd)  # 点击添加标签按钮
        self.ui.lab_pB_delLabel.clicked.connect(self.labelDel)  # 点击删除标签按钮
        self.ui.Lab_lW_labelMessage.itemDoubleClicked.connect(self.labelModify)  # 双击标签item

        self.ui.tabWidget.currentChanged.connect(self.initData)

        # self.ui.lab_lW_ClassMessage.currentTextChanged.connect(self.changeDict)  # 改变字典
        # 按道理点击tab或这关闭啥的才保存！！！这里每一次操作都保存

    def labelClassAdd(self):
        '''添加标签类'''
        # dia = inputDia()  # 生成输入对话框对象
        self.inputDia.show()
        labelClassName = self.inputDia.getLabelClassText('')  # 获取用户输入
        print("labelClassName:" + labelClassName)
        if labelClassName == '':  # 用户没有输入直接返回
            return None
        # 判断是否已经存在该标签类！！！并提醒
        if labelClassName in self.LabelClassDict.keys():
            QMessageBox.warning(
                None,
                '警告',
                '当前标签类已存在，请重新添加标签类！')
            return None

        self.ui.lab_lW_ClassMessage.addItem(labelClassName)  # 在listWidget添加item
        self.LabelClassDict[labelClassName] = []  # 添加进字典
        self.jsonIO.writeJson(self.LabelClassDict)  # 写入json文件
        # 修改csv文件的内容
        self.commentData[labelClassName] = '待标注'
        self.commentData.to_csv(self.filePath, index=None)

        # 下面这些输出控制台方便查看的，没什么用
        print(self.LabelClassDict.items())


    def labelClassDel(self):
        '''删除标签类'''
        if 0 == self.ui.lab_lW_ClassMessage.count():  # 标签类的listWidget为空的话，提醒并返回
            QMessageBox.warning(
                None,
                '警告',
                '当前标签类为空，请添加标签类并选中后再执行删除操作！')
            return None

        item = self.ui.lab_lW_ClassMessage.currentItem()  # 获取当前点击的item对象
        if None == item:  # 若用户没有点击item，则弹出提醒并返回
            QMessageBox.warning(
                None,
                '警告',
                '请选择一个标签类后再进行删除！')
            return None
        labelClassName = item.text()  # 获取当前点击item对象的内容

        self.ui.lab_lW_ClassMessage.takeItem(self.ui.lab_lW_ClassMessage.row(item))  # 从listWidget中删除item
        del self.LabelClassDict[labelClassName]  # 从字典中删除标签类

        self.ui.Lab_lW_labelMessage.clear()  # 并清空标签的listWidget的内容
        self.jsonIO.writeJson(self.LabelClassDict)  # 写入json文件
        # 修改csv文件的内容
        del self.commentData[labelClassName]
        self.commentData.to_csv(self.filePath, index=None)

        # 下面这些输出控制台方便查看的，没什么用
        print(self.LabelClassDict.items())

    def labelClassModify(self):
        '''修改标签类'''
        '''item = self.ui.lab_lW_ClassMessage.currentItem()  # 获取当前点击的item对象
        ind = self.ui.Lab_lW_labelMessage.row(item)
        className = item.text()
        print('1:' + className)
        self.ui.lab_lW_ClassMessage.currentTextChanged.connect(self.changeDict)  # 改变字典'''

        # print(item)
        item = self.ui.lab_lW_ClassMessage.currentItem()  # 获得当前标签类
        oldLabelClassName = item.text()  # 获得当前标签类的内容
        ind = self.ui.lab_lW_ClassMessage.row(item)  # 获得当前标签类在listWidget的位置

        # dia = inputDia()
        self.inputDia.show()
        newLabelClassName = self.inputDia.getLabelClassText(oldLabelClassName)  # 获取用户输入
        if '' == newLabelClassName:  # 用户没有输入直接返回
            return None
        # 判断是否已经存在该标签类！！！并提醒
        if newLabelClassName in self.LabelClassDict.keys():
            QMessageBox.warning(
                None,
                '警告',
                '当前标签类已存在，请重新添加标签类！')
            return None

        self.ui.lab_lW_ClassMessage.takeItem(ind)  # 从listWidget删除当前标签类
        self.ui.lab_lW_ClassMessage.insertItem(ind, newLabelClassName)  # 在原来位置添加新标签类
        self.LabelClassDict[newLabelClassName] = self.LabelClassDict.pop(oldLabelClassName)  # 修改字典key
        self.jsonIO.writeJson(self.LabelClassDict)  # 写入json文件
        # 修改csv文件
        self.commentData = self.commentData.rename(columns={oldLabelClassName: newLabelClassName})
        self.commentData.to_csv(self.filePath, index=None)

        # 下面这些输出控制台方便查看的，没什么用
        print(self.LabelClassDict.items())

    '''def close_edit(self,item):
        try:
            val = self.ui.lab_lW_ClassMessage.item(self.ui.lab_lW_ClassMessage.currentRow())
            self.ui.lab_lW_ClassMessage.closePersistentEditor(val)
        except Exception as E:
            print(E)'''

    def classConnectLabel(self):
        '''标签类和标签产生联系，主要是切换标签类的时候要相应的修改标签的显示'''
        # 查看ui的内容和字典的是否一直，不一致则修改
        '''for index in range(self.ui.lab_lW_ClassMessage.count()):
            item = self.ui.lab_lW_ClassMessage.item(index)
            if item.text() not in self.LabelClassDict.keys():
                ind = self.ui.Lab_lW_labelMessage.row(item)
                className = item.text()
                key = self.LabelClassDict.keys()
                print(key)
                self.LabelClassDict[className] = self.LabelClassDict.pop(key)  # 修改字典key
                self.jsonIO.writeJson(self.LabelClassDict)  # 写入json文件
                break'''

        self.ui.Lab_lW_labelMessage.clear()  # 清除标签的listWidget
        item = self.ui.lab_lW_ClassMessage.currentItem()  # 获取当前标签类的item
        # self.ui.lab_lW_ClassMessage.openPersistentEditor(item)
        # self.ui.lab_lW_ClassMessage.currentTextChanged.connect(self.close_edit)
        # item.setFlags(item.flags() or Qt.ItemIsEditable)
        # item.setFlags(Qt.ItemIsEditable)
        LabelClassName = item.text()  # 获取当前标签类的名字
        for labelName in self.LabelClassDict[LabelClassName]:  # 对标签类的每一个标签进行显示
            self.ui.Lab_lW_labelMessage.addItem(labelName)

        # 下面这些输出控制台方便查看的，没什么用
        print(self.LabelClassDict.items())

    def labelAdd(self):
        '''添加标签'''
        item = self.ui.lab_lW_ClassMessage.currentItem()  # 找到当前标签类，便于修改字典和查重
        LabelClassName = item.text()

        # dia = inputDia()
        self.inputDia.show()
        labelName = self.inputDia.getLabelText('')  # 获取用户输入
        if '' == labelName:  # 用户没有输入直接返回
            return None
        # 判断是否已经存在该标签！！！并提醒
        if labelName in self.LabelClassDict[LabelClassName]:
            QMessageBox.warning(
                None,
                '警告',
                '当前标签已存在，请重新添加标签！')
            return None

        self.ui.Lab_lW_labelMessage.addItem(labelName)  # 在标签的listWidget添加新标签

        self.LabelClassDict[LabelClassName].append(labelName)  # 修改字典
        self.jsonIO.writeJson(self.LabelClassDict)  # 写入json文件

        # 下面这些输出控制台方便查看的，没什么用
        print(self.LabelClassDict.items())

    def labelDel(self):
        '''删除标签'''
        if 0 == self.ui.Lab_lW_labelMessage.count():  # 标签的listWidget为空的话，提醒并返回
            QMessageBox.warning(
                None,
                '警告',
                '请选择标签类或者添加标签并选中标签后再执行删除操作！')
            return None

        item2 = self.ui.Lab_lW_labelMessage.currentItem()  # 获取当前点击的标签的item
        if None == item2:  # 若用户没有点击item，则弹出提醒并返回
            QMessageBox.warning(
                None,
                '警告',
                '请选择一个标签后再进行删除！')
            return None
        labelName = item2.text()

        item1 = self.ui.lab_lW_ClassMessage.currentItem()  # 获取当前点击的标签类item对象，为了修改字典
        LabelClassName = item1.text()

        self.ui.Lab_lW_labelMessage.takeItem(self.ui.Lab_lW_labelMessage.row(item2))  # 修改标签的listWidget
        self.LabelClassDict[LabelClassName].remove(labelName)  # 修改字典
        self.jsonIO.writeJson(self.LabelClassDict)  # 写入json文件

        # 下面这些输出控制台方便查看的，没什么用
        print(self.LabelClassDict.items())

    def labelModify(self):
        '''修改标签'''
        item1 = self.ui.lab_lW_ClassMessage.currentItem()  # 获取当前标签类
        LabelClassName = item1.text()

        item = self.ui.Lab_lW_labelMessage.currentItem()  # 获取当前标签
        oldLabelName = item.text()
        ind = self.ui.Lab_lW_labelMessage.row(item)

        # dia = inputDia()
        self.inputDia.show()
        labelName = self.inputDia.getLabelText(oldLabelName)
        if '' == labelName:  # 用户没有输入直接返回
            return None
        # 判断是否已经存在该标签！！！并提醒
        if labelName in self.LabelClassDict[LabelClassName]:
            QMessageBox.warning(
                None,
                '警告',
                '当前标签已存在，请重新添加标签！')
            return None

        self.ui.Lab_lW_labelMessage.takeItem(ind)  # 删除
        self.ui.Lab_lW_labelMessage.insertItem(ind, labelName)  # 插入

        self.LabelClassDict[LabelClassName].remove(oldLabelName)  # 修改字典，删除原有的
        # self.LabelClassDict[LabelClassName].append(labelName)  # 添加，这里应该用insert！！！
        self.LabelClassDict[LabelClassName].insert(ind, labelName)  # 添加
        self.jsonIO.writeJson(self.LabelClassDict)  # 写入json文件

        # 下面这些输出控制台方便查看的，没什么用
        print(self.LabelClassDict.items())


class inputDiaClass(QDialog, inputDia.Ui_Dialog):
    def __init__(self):
        super(inputDiaClass, self).__init__()
        self.setupUi(self)
        # self.start()
        # self.text = "111"

        '''app = QApplication(sys.argv)
        self.Dialog = QDialog()
        self.ui = inputDia.Ui_Dialog()
        self.ui.setupUi(self.Dialog)'''
        # self.Dialog.show()
        # sys.exit(app.exec_())

    '''def start(self):
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        self.text = self.lineEdit.text()
        print(self.text)
        self.close()

    def reject(self):
        # self.destroy()
        self.close()'''

    def getLabelClassText(self, curText):
        '''标签类的输入对话框'''

        '''text, okPressed = self.diaClass.getText(self.diaClass, "添加标签类", "请输入标签类名:", QLineEdit.Normal, "")
        if okPressed and text:
            print(text)
        return text'''
        self.setWindowTitle('标签类')
        self.label.setText('请输入标签类名：')
        self.lineEdit.setText(curText)
        if self.exec_():  # accept 则返回1，reject返回0
            text = self.lineEdit.text()
            return text
        else:
            return ''

    def getLabelText(self, curText):
        '''标签的输入对话框'''

        '''text, okPressed = self.getText(self, "添加标签", "请输入标签名:", QLineEdit.Normal, "")
        if okPressed and text:
            print(text)
        return text'''
        self.setWindowTitle('标签')
        self.label.setText('请输入标签名：')
        self.lineEdit.setText(curText)
        if self.exec_():  # accept 则返回1，reject返回0
            text = self.lineEdit.text()
            return text
        else:
            return ''
