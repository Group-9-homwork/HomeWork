import requests
import re
import time
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QWidget, QMessageBox, QDialog
from PyQt5.QtCore import Qt
import pandas as pd
import threading
import os

from code.File import FileIO
import GlobalValues as gv
from PyQt5.QtWidgets import QFileDialog


class SpiderModule():
    def __init__(self, ui):
        self.ui = ui
        self.ui.spi_pB_stop.setEnabled(False);
        self.initArgs()

    def initArgs(self):
        '''初始化一些参数'''
        self.query = {
            "u": 8580808395,
            "uuid": 1387233616647565312,
            "count": 10,
            "comment": 0,
            "symbol": "SH603517",
            "hl": 0,
            "source": "all",
            "sort": "",
            "page": 1,
            "q": "",
            "type": 11,
            "session_token": "null",
            "access_token": "1d297d0adc829df80cc2cf02eef605b275ac2a90",
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        self.query['symbol'] = "SH603517"  # 股票代码
        self.baseUrl = 'https://xueqiu.com/query/v1/symbol/search/status?'  # 基础URL
        self.pageComment = 10  # 一页共几条
        self.totalPage = 10  # 总业数
        self.flag = 1  # 开始暂停的标志
        self.curPage = 1  # 第几页
        self.curComment = 1  # 第几条
        self.curK = 1  # 第几条
        self.fileio = FileIO()  # 文件的读写操作
        self.noPage = 0  # 页面是否获取
        self.end = 0  # 是否结束线程爬虫
        self.fileIO = FileIO()

    def spiderStart(self):
        '''添加信号和槽'''
        self.ui.spi_pB_yes.clicked.connect(self.startCrawler)  # 开始爬虫
        self.ui.spi_pB_stop.clicked.connect(self.stopCrawler)  # 停止爬虫
        # 修改linetext的内容就会发生cur变1
        self.ui.spi_lE_stock.textChanged.connect(self.changeCur)  # 股票代码文本内容改变
        self.ui.spi_lE_path.textChanged.connect(self.changeCur)  # 路径文本内容改变
        self.ui.spi_pB_open.clicked.connect(self.openFile)  # 打开文件

    def openFile(self):
        self.filePath, _ = QFileDialog.getOpenFileName(
            None,  # 父窗口对象
            "打开文件",  # 标题
            "./",  # 起始目录
            # "文件类型 (*.csv)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.spi_lE_path.setText(self.filePath)
        print(self.filePath)

    def changeCur(self):
        '''文本内容改变就从第一页第一条开始爬'''
        self.curPage = 1
        self.curComment = 1
        # 终止当前线程！！！
        self.end = 1
        self.curK = 1
        # print(1111111)

    def stopCrawler(self):
        '''停止爬虫'''
        # 设置文本输入框为可编辑
        # self.ui.spi_lE_stock.setFocusPolicy(Qt.Focus)
        # self.ui.spi_lE_path.setFocusPolicy(Qt.Focus)
        self.ui.spi_lE_stock.setReadOnly(False)
        self.ui.spi_lE_path.setReadOnly(False)

        # 设置按钮不可点击
        self.ui.spi_pB_yes.setEnabled(True);
        self.ui.spi_pB_open.setEnabled(True);
        self.ui.spi_pB_stop.setEnabled(False);

        self.flag = 0

    def startCrawler(self, flag):
        '''开始爬虫'''
        # 设置文本输入框为不可编辑
        self.ui.spi_lE_stock.setReadOnly(True)
        self.ui.spi_lE_path.setReadOnly(True)

        # 设置按钮不可点击
        self.ui.spi_pB_yes.setEnabled(False);
        self.ui.spi_pB_open.setEnabled(False);
        self.ui.spi_pB_stop.setEnabled(True);

        # 获取界面输入
        self.stock = self.ui.spi_lE_stock.text()
        self.filePath = self.ui.spi_lE_path.text()
        print(self.stock)
        print(self.filePath)

        # 正则表达式匹配是否是股票代码和csv文件
        if not re.search('^[A-Z]{2}[0-9]{6}', self.stock):
            QMessageBox.warning(
                None,
                '警告',
                '股票代码格式错误，请重新输入！')
            # 设置文本输入框为可编辑
            # self.ui.spi_lE_stock.setFocusPolicy(Qt.Focus)
            # self.ui.spi_lE_path.setFocusPolicy(Qt.Focus)
            self.ui.spi_lE_stock.setReadOnly(False)
            self.ui.spi_lE_path.setReadOnly(False)

            # 设置按钮不可点击
            self.ui.spi_pB_yes.setEnabled(True);
            self.ui.spi_pB_open.setEnabled(True);
            self.ui.spi_pB_stop.setEnabled(False);
            return

        if not re.search('^((?:[a-zA-Z]:)?\/(?:[^\\\?\/\*\|<>:"]+\/)+)', self.filePath):
            print(self.filePath)
            QMessageBox.warning(
                None,
                '警告',
                '文件路径错误，请重新输入！')
            # 设置文本输入框为可编辑
            self.ui.spi_lE_stock.setReadOnly(False)
            self.ui.spi_lE_path.setReadOnly(False)

            # 设置按钮不可点击
            self.ui.spi_pB_yes.setEnabled(True);
            self.ui.spi_pB_open.setEnabled(True);
            self.ui.spi_pB_stop.setEnabled(False);
            return

        if not re.search('\.csv$', self.filePath):
            QMessageBox.warning(
                None,
                '警告',
                '文件类型错误，请选择csv文件！')
            # 设置文本输入框为可编辑
            self.ui.spi_lE_stock.setReadOnly(False)
            self.ui.spi_lE_path.setReadOnly(False)

            # 设置按钮不可点击
            self.ui.spi_pB_yes.setEnabled(True);
            self.ui.spi_pB_open.setEnabled(True);
            self.ui.spi_pB_stop.setEnabled(False);
            return

        f = open(self.filePath, 'a+')  # 如果不存在则创建一个
        f.close()

        '''if '' == self.stock or '' == self.filePath:
            self.stock = "SH603517"
            self.filePath = "./data.csv"
        print('33333')'''

        # 更新全局变量
        '''gv.set_value("stock", self.stock)
        print(111)
        gv.set_value("filePath", self.filePath)
        print(gv.get_value('stock'))
        print(gv.get_value('filePath'))'''

        # 输出开始爬虫
        self.ui.spi_tB_message.append('开始爬虫\n股票代码：'+self.stock+'\n当前文件路径：'+self.filePath + '\n')
        '''self.ui.cursor = ui.spi_tB_message.textCursor()
        self.ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        self.ui.spi_tB_message.ensureCursorVisible()'''

        # 提取出时间，用来防止重复读，这里排序下感觉会更好
        self.commentData = self.fileIO.readCsv(self.filePath)
        self.commentTime = (self.commentData['时间']).values.tolist()  # 用来防止重复读，其实转化成数字更好

        '''if dfFile1Tmp.empty or dfFile2Tmp.empty:
            QMessageBox.warning(
                None,
                '警告',
                '比较文件里没有数据！')
            return'''

        self.query['symbol'] = self.stock
        self.flag = 1
        # 开启一个线程处理
        t = threading.Thread(target = self.parse)
        t.start()
        # t.join()
        # self.parse()
        if self.noPage:
            QMessageBox.warning(
                None,
                '警告',
                '股票代码可能不存在，请仔细检查')
            self.noPage = 0
        flag = 1
        return flag

    '''def display(self, content):
        self.ui.spi_tB_message.append("第" + "条")
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.userName)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.text)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.source)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.created_at)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.retweet_count)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.reply_count)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.reward_count)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append(content.fav_count)
        self.ui.spi_tB_message.ensureCursorVisible()
        self.ui.spi_tB_message.append("-" * 50)
        self.ui.spi_tB_message.ensureCursorVisible()'''

    def getUrl(self, pageNum):
        '''获取URL'''
        self.query['page'] = pageNum
        str1 = json.dumps(self.query)
        str1 = str1.translate(str1.maketrans({":": "=", ",": "&", "\"": "", " ": "", "{": "", "}": ""}))
        pageUrl = self.baseUrl + str1
        # print(pageUrl)
        return pageUrl

    def getPage(self, url):
        '''获取页面'''
        try:
            req = requests.get(url, headers=self.headers)  # 获取页面
            req.raise_for_status()
            page = json.loads(req.text)
        except:
            QMessageBox.warning(
                None,
                '警告',
                '股票代码可能不存在，请仔细检查')
            print("getPage Error!")
            return None
        return page

    def parse(self):
        '''解析页面获取内容'''
        contents = []
        k = self.curK  # 记录爬取第几条的
        i = self.curPage
        while i <= self.totalPage:
            pageUrl = self.getUrl(i)  # 获取网页url
            # print(pageUrl)
            page = self.getPage(pageUrl)  # 获取页面内容
            # print(page)
            if page == None:
                self.noPage = 1
                # 设置文本输入框为可编辑
                # self.ui.spi_lE_stock.setFocusPolicy(Qt.Focus)
                # self.ui.spi_lE_path.setFocusPolicy(Qt.Focus)
                self.ui.spi_lE_stock.setReadOnly(False)
                self.ui.spi_lE_path.setReadOnly(False)

                # 设置按钮不可点击
                self.ui.spi_pB_yes.setEnabled(True);
                self.ui.spi_pB_open.setEnabled(True);
                self.ui.spi_pB_stop.setEnabled(False);
                return []
            if page['list'] == []:
                self.noPage = 1
                # 设置文本输入框为可编辑
                # self.ui.spi_lE_stock.setFocusPolicy(Qt.Focus)
                # self.ui.spi_lE_path.setFocusPolicy(Qt.Focus)
                self.ui.spi_lE_stock.setReadOnly(False)
                self.ui.spi_lE_path.setReadOnly(False)

                # 设置按钮不可点击
                self.ui.spi_pB_yes.setEnabled(True);
                self.ui.spi_pB_open.setEnabled(True);
                self.ui.spi_pB_stop.setEnabled(False);
                return []

            j = self.curComment
            self.curComment = 1
            while j <= self.pageComment:
                # userName = page['list'][j]['user']['screen_name']
                text = page['list'][j - 1]['text']
                # 用正则表达式，过滤掉一些东西
                text = re.sub('<a.*?</a>', '', text)
                text = re.sub('<.*?>', '', text)
                text = re.sub('&\w{2}sp;', '', text)

                '''source = page['list'][j]['source']  # 来源'''

                tracks = json.loads(page['list'][j - 1]['trackJson'])
                created_at = tracks['created_at']  # 发表评论时间
                # print(created_at)
                '''retweet_count = tracks['retweet_count']  # 转发数
                reply_count = tracks['reply_count']  # 评论数
                reward_count = tracks['reward_count']  # 点赞数
                fav_count = tracks['fav_count']  # 收藏数'''

                if created_at in self.commentTime:
                    j = j + 1
                    continue

                # content = Content(userName, text, source, created_at, retweet_count, reply_count, reward_count, fav_count)
                content = Content(text, created_at)
                contents.append(content)

                content.printData(self.ui, k)  # 输出到界面
                k = k + 1
                j = j + 1

                # 结束爬虫
                if 0 == self.flag:
                    self.curPage = i
                    self.curComment = j
                    self.curK = k
                    # 跳出多重循环
                    i = self.totalPage + 1
                    j = self.pageComment + 1

                time.sleep(3)  # 防止反爬
            i = i + 1

        # 保存
        if contents == None:
            # 设置文本输入框为可编辑
            # self.ui.spi_lE_stock.setFocusPolicy(Qt.Focus)
            # self.ui.spi_lE_path.setFocusPolicy(Qt.Focus)
            self.ui.spi_lE_stock.setReadOnly(False)
            self.ui.spi_lE_path.setReadOnly(False)

            # 设置按钮不可点击
            self.ui.spi_pB_yes.setEnabled(True);
            self.ui.spi_pB_open.setEnabled(True);
            self.ui.spi_pB_stop.setEnabled(False);
            return
        # 把content转化为字典
        dataDict = {'时间': [], '评论': []}
        for content in contents:
            dataDict['时间'].append(content.created_at)
            print(content.created_at)
            dataDict['评论'].append(content.text)
            print(content.text)
        # 写入文件
        self.fileio.writeCsv(self.filePath, dataDict)  # 路径和字典参数
        if 0 == self.flag:
            self.ui.spi_tB_message.append('爬虫暂停\n')
            self.ui.cursor = self.ui.spi_tB_message.textCursor()
            self.ui.spi_tB_message.moveCursor(self.ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
            QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
            self.ui.spi_tB_message.ensureCursorVisible()
        return contents


class Content():
    def __init__(self, text, created_at):
        # self.userName = userName  # 用户名
        self.text = text  # 评论内容
        # self.source = source  # 来源
        self.created_at = created_at  # 创建时间
        '''self.retweet_count = retweet_count
        self.reply_count = reply_count
        self.reward_count = reward_count
        self.fav_count = fav_count'''

    '''def printData(self):
        print('用户名：' + self.userName)
        print('评论内容：' + self.text)
        print('来源：' + self.source)
        print('创建时间：' + self.created_at)
        print('转发数：' + str(self.retweet_count))
        print('评论数：' + str(self.reply_count))
        print('点赞数：' + str(self.reward_count))
        print('收藏数：' + str(self.fav_count))
        print("-" * 50)'''

    def printData(self, ui, i):
        '''UI输出数据'''
        ui.spi_tB_message.append("第" + str(i) + "条")
        '''ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        ui.spi_tB_message.append('用户名：' + self.userName)
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()'''

        tmpText = self.text
        if len(tmpText) > 50:
            tmpText = tmpText[:50] + '...'
        ui.spi_tB_message.append('评论内容：' + tmpText + '\n')

        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        '''ui.spi_tB_message.append('来源：' + self.source)
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        ui.spi_tB_message.append('创建时间：' + self.created_at)
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        ui.spi_tB_message.append('转发数：' + str(self.retweet_count))
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        ui.spi_tB_message.append('评论数：' + str(self.reply_count))
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        ui.spi_tB_message.append('点赞数：' + str(self.reward_count))
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        ui.spi_tB_message.append('收藏数：' + str(self.fav_count))
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()

        ui.spi_tB_message.append("-" * 50)
        ui.cursor = ui.spi_tB_message.textCursor()
        ui.spi_tB_message.moveCursor(ui.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        ui.spi_tB_message.ensureCursorVisible()'''
