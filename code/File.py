import os
import csv
from Spider import *

class FileIO():

    def __init__(self):
        self.filePath = r'./data.csv'

    def readFile(self, path):
        if path:
            self.filePath = path
        # 判断文件是否存在。。。

        with open(self.filePath, "r") as f:
            for line in f.readlines():
                print(line)

    def writeFile(self, path, contents):
        if path:
            self.filePath = path
        print(self.filePath)

        with open(path, 'a+') as f:
            for content in contents:
                f.write(f'{content.userName},{content.text}, {content.source}, {content.created_at}, {content.retweet_count},{content.reply_count}, {content.reward_count}, {content.fav_count}\n')

        return