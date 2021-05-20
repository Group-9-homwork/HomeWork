import unittest
import sys
from code import MainUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit

from code.Spider import SpiderModule, Content


class MyTestCase(unittest.TestCase):
    '''def test_spiderStart(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        spider = SpiderModule(ui)
        spider.spiderStart()
        a = SpiderModule
        result = a.spiderStart(0)
        self.assertEqual(result, 1)'''

    def test_startCrawler(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        spider = SpiderModule(ui)
        spider.spiderStart()
        spider.totalPage=1
        ui.spi_lE_stock.setText(r'SH603517')
        ui.spi_lE_path.setText(r'D:\test\HomeWork\test\data2.csv')
        result = spider.startCrawler(flag=0)

        self.assertEqual(result, 1)

    '''def test_display(self):
        self.assertEqual(True, True)
    '''

    '''def test_printData(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        spider = SpiderModule(ui)
        spider.spiderStart()
        a = Content('1', '1')
        result = a.printData(ui, 1)
        self.assertEqual(result, 1)'''

    def test_getUrl(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        spider = SpiderModule(ui)
        spider.spiderStart()
        # baseUrl = 'https://xueqiu.com/query/v1/symbol/search/status?'
        pageNum = 12
        url = 'https://xueqiu.com/query/v1/symbol/search/status?u=8580808395&uuid=1387233616647565312&count=10&comment=0&symbol=SH603517&hl=0&source=all&sort=&page=12&q=&type=11&session_token=null&access_token=1d297d0adc829df80cc2cf02eef605b275ac2a90'
        str = spider.getUrl(pageNum)
        self.assertEqual(str, url)

    def test_getPage(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        spider = SpiderModule(ui)
        spider.spiderStart()
        page = spider.getPage('https://xueqiu.com/query/v1/symbol/search/status?u=8580808395&uuid=1387233616647565312&count=10&comment=0&symbol=SH603517&hl=0&source=all&sort=&page=12&q=&type=11&session_token=null&access_token=1d297d0adc829df80cc2cf02eef605b275ac2a90')
        # b = type(page)
        b = {}
        self.assertEqual(type(page), type(b))

    def test_parse(self):
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = MainUI.Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        spider = SpiderModule(ui)
        spider.spiderStart()
        '''siteData = ['StockComment', 'https://xueqiu.com/query/v1/symbol/search/status?', 10, 10]  # 网页参数
        sites = []  # 通过提供的参数生成的Wedsite对象
        sites.append(Website(siteData[0], siteData[1], siteData[2], siteData[3]))'''
        spider.totalPage = 1
        ui.spi_lE_stock.setText(r'SH603517')
        ui.spi_lE_path.setText(r'D:\test\HomeWork\test\data2.csv')
        spider.startCrawler(flag=0)
        result = spider.parse()
        b = []
        self.assertEqual(type(result), type(b))

if __name__ == '__main__':
    unittest.main()
